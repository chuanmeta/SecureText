
from fastapi import FastAPI
from text_service import random_text

app = FastAPI()

@app.get("/welcome")
def hello(name: str = "Việt Nam"):
    return {
        "text": random_text()
    }