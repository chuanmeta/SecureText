
from fastapi import FastAPI
from .services import io_service as io

app = FastAPI()
RES_ROOT = "res"
FONTS_ROOT = f"{RES_ROOT}/fonts"

@app.get("/")
def info():
    return {
        "name": "appname"
    }

@app.get("/mkdir")
def fonts():
    return {
        "path": io.createDirectory(FONTS_ROOT)
    }