from fastapi import APIRouter

router = APIRouter("/users")

@router.get("/{name}")
def welcome(name: str):
    return {
        "message": f"welcome {name} to with my app."
    }

@router.get("/", response_class=PlainTextResponse)
def hello() -> str:
    return "Hello, can i help you?"