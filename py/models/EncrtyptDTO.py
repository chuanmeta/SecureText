from pydantic import BaseModel

class EncryptDTO(BaseModel):
    text: str
    fontName: str