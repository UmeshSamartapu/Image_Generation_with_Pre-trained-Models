import os
import torch
from datetime import datetime

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from diffusers import StableDiffusionPipeline
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize model once at startup
@app.on_event("startup")
async def load_model():
    global pipe
    try:
        model_id = "runwayml/stable-diffusion-v1-5"

        if os.getenv("HF_AUTH_TOKEN"):
            from huggingface_hub import login
            login(token=os.getenv("HF_AUTH_TOKEN"))

        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"⏳ Initializing model on {device}...")

        if device == "cuda":
            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float16,
                use_safetensors=True
            ).to("cuda")
            pipe.enable_attention_slicing()
            pipe.enable_model_cpu_offload()
        else:
            pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float32,
                use_safetensors=True
            ).to("cpu")

        print("✅ Model loaded successfully")

    except Exception as e:
        print(f"❌ Error loading model: {str(e)}")
        raise

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Initialize model once at startup
@app.on_event("startup")
async def load_model():
    global pipe
    # ... [keep existing model loading code] ...

@app.post("/generate", response_class=HTMLResponse)
async def generate_image(
    request: Request,
    prompt: str = Form(...),
    steps: int = Form(50)
):
    try:
        start_time = datetime.now()
        print(f"🎨 Generating image for prompt: {prompt}")
        
        # Generate image
        image = pipe(prompt, num_inference_steps=steps).images[0]
        
        # Create unique folder using timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_dir = os.path.join("static/generations", timestamp)
        os.makedirs(output_dir, exist_ok=True)
        
        # Save image
        image_path = os.path.join(output_dir, "output.png")
        image.save(image_path)
        
        # Calculate generation time
        time_taken = datetime.now() - start_time
        generation_time = f"{time_taken.total_seconds():.2f} seconds"

        return templates.TemplateResponse("index.html", {
            "request": request,
            "image_url": f"/static/generations/{timestamp}/output.png",
            "prompt": prompt,
            "generation_time": generation_time,
            "timestamp": timestamp
        })
    except Exception as e:
        print(f"❌ Generation error: {str(e)}")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)