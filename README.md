# 🐳 FastAPI + Hugging Face Docker API

A containerized REST API that performs AI text generation using a Hugging Face model, built with FastAPI and deployed with Docker.

---

## 🚀 What it does

Send a text prompt to the API and get AI-generated text back — all running inside a Docker container.

```
Your Request → Docker Container → FastAPI → Hugging Face Model → AI Response
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| 🐳 Docker | Containerization |
| ⚡ FastAPI | REST API framework |
| 🤗 Hugging Face Transformers | AI text generation |
| 🐍 Python 3.13 | Programming language |
| 🦄 Uvicorn | ASGI server |

---

## 📁 Project Structure

```
fastapi-huggingface-docker/
├── app.py              # FastAPI app with Hugging Face model
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container recipe
└── README.md           # Project documentation
```

---

## ⚙️ Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

---

## 🏃 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Abdul769469/fastapi-huggingface-docker.git
cd fastapi-huggingface-docker
```

### 2. Build the Docker image
```bash
docker build -t hf-text-api .
```

### 3. Run the container
```bash
docker run -p 8000:8000 hf-text-api
```

### 4. Test the API
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"Once upon a time\", \"max_length\": 50}"
```

---

## 📡 API Endpoints

### `GET /`
Health check — confirms the server is running.

**Response:**
```json
{"status": "running"}
```

---

### `POST /generate`
Generate text from a prompt using the Hugging Face model.

**Request body:**
```json
{
  "text": "Once upon a time",
  "max_length": 50
}
```

**Response:**
```json
{
  "generated": "Once upon a time there was a..."
}
```

---

## 🖥️ Interactive API Docs

FastAPI automatically generates interactive documentation. Once the container is running, open your browser and go to:

```
http://localhost:8000/docs
```

---

## 🤗 Model

This project uses [`sshleifer/tiny-gpt2`](https://huggingface.co/sshleifer/tiny-gpt2) — a lightweight GPT-2 model from Hugging Face, ideal for testing and development on CPU.

---

## 🐳 Docker Commands Reference

| Command | Description |
|---|---|
| `docker build -t hf-text-api .` | Build the image |
| `docker run -p 8000:8000 hf-text-api` | Run the container |
| `docker ps` | List running containers |
| `docker stop <container_id>` | Stop a container |
| `docker system prune -a -f` | Clean unused images and cache |

---

## 👨‍💻 Author

**Abdul** — Built as a hands-on Docker learning project.

---

## 📄 License

MIT License