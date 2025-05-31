import random

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: list[dict]

openings = [
    "Hello! How can I assist you today?",
    "Hi there! Do you have any questions or need support?",
    "Good day! I'm ready to answer your questions.",
    "Hey! How can I accompany you today?",
    "Nice to see you! Ask me anything, and I'll try to help."
]

closings = [
    "Thank you for the chat! If you need more help, I'm here.",
    "Have a great day! Come back anytime you need something.",
    "That's all from me — good luck!",
    "You can always return if more questions arise.",
    "Talk to you later! Wishing you success in your endeavors."
]

@app.post("/api/chat")
def chat_with_ollama(request: ChatRequest):
    try:
        user_messages = request.messages

        if not user_messages or user_messages[0]["role"] != "system":
            greeting = {"role": "system", "content": random.choice(openings)}
            user_messages.insert(0, greeting)


        keywords = [
            "clothes", "clothing", "shirt", "pants", "dress", "shoes", "store",
            "delivery", "shipping", "payment", "return", "refund", "order", "size"
        ]


        last_user_message = next((m["content"] for m in reversed(user_messages) if m["role"] == "user"), "")

        if not any(kw in last_user_message.lower() for kw in keywords):
            return {
                "message": {
                    "role": "assistant",
                    "content": "I'm sorry, but I can only respond to questions related to shopping, clothing, or store-related topics. Please ask something within that scope."
                }
            }

        user_messages.insert(0, {
            "role": "system",
            "content": "Only respond to questions related to shopping, clothing, product sizes, shipping, payment, or returns. Politely refuse to answer unrelated topics."
        })

        payload = {
            "model": "tinyllama",
            "messages": user_messages,
            "stream": False
        }

        response = requests.post(
            "http://localhost:11434/api/chat",
            json=payload
        )

        response_json = response.json()

        if "message" in response_json:
            response_json["message"]["content"] += "\n\n" + random.choice(closings)

        return response_json

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
