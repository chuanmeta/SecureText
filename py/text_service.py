import random

TEXT_POOL = [
    "Xin chào Việt Nam",
    "Hello Spring Boot",
    "Hi Angular",
    "Docker compose nội bộ",
    "Font swap endcode"
]

def random_text() -> str:
    return random.choice(TEXT_POOL)
