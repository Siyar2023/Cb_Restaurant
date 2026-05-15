
from Fullstack_App_cb import chatbot_response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# allows the frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API works!"}

@app.post("/chat")
def chat(message: Message):

    user_text = message.text

    # temporary answer
    bot_response = chatbot_response(user_text)

    return {
        "response": bot_response
    }