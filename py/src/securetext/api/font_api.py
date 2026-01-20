from fastapi import APIRouter

from securetext.services import font_service as fs
from py.src.securetext.models.encrypt_request import EncryptRequest

router = APIRouter(prefix="/font")

@router.get("/create-font/{nameRootFont}")
def createFont(nameRootFont: str):
    return {
        "font": fs.generateAndSaveFont(nameRootFont, fs.generateMapping(0xE000))
    }

@router.post("/encrypt")
def encrypt(req: EncryptRequest):
    return {
        "font": fs.getFont(req.font),
        "data": fs.encode(req.text, req.fontName)
    }