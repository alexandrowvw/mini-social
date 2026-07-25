from fastapi import Depends

from app.database.session import get_session
from app.repositories.post_repository import PostRepository
from app.services.post_service import PostService

def get_post_service(
        session = Depends(get_session)
):
    repository = PostRepository(session)
    
    return PostService(repository)