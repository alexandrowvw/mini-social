# Его задача:

# - Создать подключение к PostgreSQL.
# - Создать фабрику сессий.
# - Дать FastAPI способ получать сессию через Depends.

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL
)

session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False # после commit не стирает данные объекта из памяти, оставив его актуальным
)

print(settings.DATABASE_URL)

async def get_session():
    async with session_maker() as session:
        yield session