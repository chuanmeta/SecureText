import uvicorn
from securetext.app import createApp

app = createApp()

if __name__ == "__main__":
    uvicorn.run(
        "securetext.main:app",
        host="0.0.0.0",
        port=8000
    )

