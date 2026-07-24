from app.repositories.post_repository import PostRepository
from app.services.post_service import PostService

repository = PostRepository()

def get_post_service():
    return PostService(repository)