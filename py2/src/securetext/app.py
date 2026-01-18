from fastapi import FastAPI
from securetext.api.internal.users import router

def createApp() -> FastAPI:
    return FastAPI(
        title="Internal Service",
        docs_url=None,
        redoc_url=None
    ).include_router(router, prefix="/internal")

