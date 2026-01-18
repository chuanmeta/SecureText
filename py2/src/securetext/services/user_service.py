
from securetext.models.user import User

class UserService:
    def __init__(self):
        print("Init UserService")

    def getUser(self, userId: int) -> User:
        return User(id=userId, name="chuan")