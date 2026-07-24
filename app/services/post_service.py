# бизнес проверка (правила, etc) -> repository
from app.schemas.post import PostCreate

class PostService():
    def __init__(self, repository):
        self.repository = repository

    def create_post(self, post: PostCreate):
        return self.repository.create(post.text)

    def get_posts(self):
        return self.repository.get_all_posts()