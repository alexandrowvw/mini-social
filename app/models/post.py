from datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime

from app.database.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)