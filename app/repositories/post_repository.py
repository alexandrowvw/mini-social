from sqlalchemy.ext.asyncio import AsyncSession

from app.models.post import Post

# создает пост -> postgresql
class PostRepository:
    def __init__(self, session: AsyncSession):
        self.session = session 
        
    async def create(self, text: str) -> Post:
        post = Post(
            text=text
        )

        self.session.add(post)

        await self.session.commit()
        await self.session.refresh(post)

        return post

    async def get_all_posts(self) -> list[Post]:
        pass
        # result = await self.session.execute(
        #     select(Post)
        # )

        # return result.scalars().all()