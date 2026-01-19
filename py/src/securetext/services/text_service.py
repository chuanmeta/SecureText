import uuid

def randomText(len: int) -> str:
    return uuid.uuid4().hex[:len]