from app.models.post import Post

# создает пост -> storage
class PostRepository:
    def __init__(self, session):
        self.session = session 
        
    def create(self, text: str) -> Post:
        post = Post(
            self._next_id,
            text
        )

        self._posts.append(post)
        self._next_id += 1

        return post

    def get_all_posts(self) -> list[Post]:
        return self._posts.copy()