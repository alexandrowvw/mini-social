from sqlalchemy import Column, Integer, Text

from app.database.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    text = Column(Text)