from fastapi import FastAPI
from securetext.api.internal.users import router as internal
from securetext.api.welcome import router as public

def createApp() -> FastAPI:
    app = FastAPI(
        title="Internal Service",
        docs_url=None,
        redoc_url=None
    )

    app.include_router(internal, prefix="/internal")

    return app

