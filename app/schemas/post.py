from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    text: str

class PostResponse(BaseModel):
    id: int
    text: str
    created_at: datetime