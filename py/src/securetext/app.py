from fastapi import FastAPI

from securetext.api.font_api import router

def createApp() -> FastAPI:
    app = FastAPI(
        title="Secure Text",
        docs_url=None,
        redoc_url=None
    )

    app.include_router(router, prefix="/app")

    return app