from datetime import datetime
from app.db import db
from uuid import uuid4
from pydantic import BaseModel, Field

@db.table(pk="id", indexed=["title"], tablename="todo_list")
class TodoList(BaseModel):
    """TodoList model"""

    id: int = Field(default=1, alias="id", description="TodoList id", gt=0)
    title: str = Field(max_length=63)
    description: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True