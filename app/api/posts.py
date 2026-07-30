from fastapi import APIRouter, Depends

from app.schemas.post import PostCreate, PostResponse
from app.services.post_service import PostService
from app.core.dependencies import get_post_service

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/")
async def get_posts(
    service: PostService = Depends(get_post_service)
):
    return await service.get_posts()

@router.post("/", response_model=PostResponse)
async def create_post(
    post: PostCreate,
    service: PostService = Depends(get_post_service)
):
    return await service.create_post(post)