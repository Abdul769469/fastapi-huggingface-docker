from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

generator = pipeline("text-generation", model="sshleifer/tiny-gpt2")

class Prompt(BaseModel):
    text: str
    max_length: int = 50

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/generate")
def generate(prompt: Prompt):
    result = generator(prompt.text, max_length=prompt.max_length)
    return {"generated": result[0]["generated_text"]}