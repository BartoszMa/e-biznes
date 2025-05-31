from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
app = FastAPI()

class ChatRequest(BaseModel):
    messages: list[dict]

@app.post("/api/chat")
def chat_with_ollama(request: ChatRequest):
    try:
        payload = {
            "model": "tinyllama",
            "messages": request.messages,
            "stream": False
        }

        response = requests.post(
            "http://localhost:11434/api/chat",
            json=payload
        )

        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
