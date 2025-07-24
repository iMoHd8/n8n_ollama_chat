from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(data: ChatRequest):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:latest",
            "prompt": data.prompt,
            "stream": False
        }
    )
    
    result = {"response": response.json().get("response")}

    return result