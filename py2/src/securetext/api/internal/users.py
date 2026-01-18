from fastapi import APIRouter
from securetext.services.user_service import UserService

router = APIRouter(prefix="/users")
userService = UserService()

@router.get("/{userId}")
def getUser(userId: int):
    return userService.getUser(userId)