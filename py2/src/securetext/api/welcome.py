from fastapi import APIRouter

router = APIRouter()

@router.get("/{name}")
def welcome(name: str) -> str:
    return "welcome {name} to with my app."