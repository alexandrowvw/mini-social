from datetime import datetime
from sqlalchemy import Integer, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )