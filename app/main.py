from fastapi import FastAPI

from app.api.routers import api_router as routers

app = FastAPI(
    title="Mini Social"
)

app.include_router(routers)