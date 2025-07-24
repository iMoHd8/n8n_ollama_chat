from fastapi import FastAPI
from pydantic import BaseModel
from config import OLLAMA_MODEL_ID
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(data: ChatRequest):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": OLLAMA_MODEL_ID,
            "prompt": data.prompt,
            "stream": False
        }
    )
    
    result = {"response": response.json().get("response")}

    return result