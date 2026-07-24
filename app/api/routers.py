from fastapi import APIRouter

api_router = APIRouter()

from app.api.posts import router as posts_router

api_router.include_router(posts_router)