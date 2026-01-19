from pydantic import BaseModel

class EncryptRequest(BaseModel):
    font: str
    text: str