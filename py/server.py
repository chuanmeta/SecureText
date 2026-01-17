
from fastapi import FastAPI

from services import font_service as fs

from models import EncrtyptDTO

app = FastAPI()

@app.get("/create-font")
def createFont():
    return {
        "font": fs.generateAndSaveFont(fs.generateMapping(0xE000))
    }

@app.post("/encrypt")
def encrypt(req: EncrtyptDTO):
    return {
        "font": fs.getFont(req.fontName),
        "data": fs.encode(req.text, req.fontName)
    }
