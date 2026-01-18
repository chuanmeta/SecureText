from fastapi import FastAPI
from securetext.api.internal.users import router

def createApp() -> FastAPI:
    app = FastAPI(
        title="Internal Service",
        docs_url=None,
        redoc_url=None
    )

    app.include_router(router, prefix="/internal")

    app.include_router(router, prefix="/")

    return app

