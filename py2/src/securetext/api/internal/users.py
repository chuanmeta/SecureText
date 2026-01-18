from fastapi import APIRouter
from securetext.services.user_service import UserService

router = APIRouter(prefix="/users")

@router.get("/{userId}")
def getUser(userId: int):
    return UserService.getUser(userId)