# бизнес проверка (правила, etc) -> repository
from app.schemas.post import PostCreate
from app.models.post import Post


class PostService():
    def __init__(self, repository):
        self.repository = repository

    async def create_post(self, post: PostCreate):
        if len(post.text) > 500:
            raise ValueError(
                "Пост слишком длинный"
            )

        if not post.text.strip():
            raise ValueError(
                "Пост не может быть пустой"
            )

        post_model = Post(
            text=post.text
        )

        return await self.repository.create(post_model)

    async def get_posts(self):
        return await self.repository.get_all_posts()