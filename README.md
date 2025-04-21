# AI Image Generation API with Stable Diffusion

[![Generated Example]( https://github.com/UmeshSamartapu/Image_Generation_with_Pre-trained-Models_ProdigyInfoTech/blob/main/static/Creative%20Image%20Studio%20pic.png )

A FastAPI-powered service for generating images from text prompts using Stable Diffusion v1.4/1.5 from Hugging Face.

## Features

- 🎨 Generate high-quality images from text prompts
- 🚀 GPU-accelerated inference with Diffusers
- 📝 Support for multiple diverse prompts in single batch
- 🌐 REST API endpoints for integration
- 🖥️ Optional Gradio web UI for interactive use
- 🔒 Secure token authentication support
- ⚡ Async-ready FastAPI backend

### Technologies Used

- **Backend:** FastAPI, Uvicorn, Python-multipart
- **ML Framework:** Diffusers, Transformers, Torch
- **Acceleration:** Accelerate, Safetensors
- **Authentication:** Hugging Face Hub, Python-dotenv
- **Deployment:** Docker (compatible), Hugging Face Spaces

## Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/stable-diffusion-api.git
cd stable-diffusion-api
```

### 2. Set up environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up Hugging Face token:
```bash
echo "HF_TOKEN=your_huggingface_token" > .env
```

## Usage

### 1.Start the API server:
```bash
uvicorn main:app --reload --port 8000
```

### 2.Access webpage
```bash
http://localhost:8000/
```

### 
```bash

```

## Project Structure
```bash
stable-diffusion-api/
├── app/
│   ├── routes/         # API endpoints
│   └── models/        # ML model handling
├── outputs/           # Generated images
├── main.py            # FastAPI application
├── gradio_ui.py       # Optional web interface
├── requirements.txt   # Dependencies
└── .env.example       # Environment template
```

## 📦 Key Endpoints

- *POST /generate:* Generate image from text prompt

## Acknowledgments
  
- Stable Diffusion by CompVis and Stability AI

- Hugging Face Diffusers library

- FastAPI community

- Maintainer: https://github.com/UmeshSamartapu

## Demo 
### You can watch the ([youtube video](   )) for demo
<p align="center">
  <img src=" https://github.com/UmeshSamartapu/Image_Generation_with_Pre-trained-Models_ProdigyInfoTech/blob/main/static/Creative%20Image%20Studio_Gif.gif " />
</p>



## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---

🔥 Always exploring new technologies and solving real-world problems with code!
