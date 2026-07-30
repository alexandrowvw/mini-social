import uvicorn
from fastapi import FastAPI

from app.api.routers import api_router as routers

app = FastAPI(
    title="Mini Social"
)

app.include_router(routers)

if __name__ == "__main__":

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )