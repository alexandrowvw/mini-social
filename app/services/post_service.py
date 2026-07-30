# бизнес проверка (правила, etc) -> repository
from app.schemas.post import PostCreate

class PostService():
    def __init__(self, repository):
        self.repository = repository

    async def create_post(self, post: PostCreate):
        return await self.repository.create(post.text)

    async def get_posts(self):
        return await self.repository.get_all_posts()