from datetime import datetime
from typing import List

from ormdantic import Ormdantic
from app.db import _init_db
from app.models import TodoList
from app.schema import TodoItem, TodoItemIn


async def create_todo(
        title: str, description: str,
        db: Ormdantic = _init_db()
) -> TodoItem:
    todo = TodoList(title=title, description=description, created_at=datetime.now(), updated_at=datetime.now())
    await db[TodoList].insert(todo)
    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "created_at": todo.created_at,
        "updated_at": todo.updated_at
    }

async def exist(id: int, db: Ormdantic = _init_db()) -> bool:
    query = db[TodoList].find_many(where={"id": id}, limit=1)
    return await query

async def delete_todo(id: int, db: Ormdantic = _init_db()) -> None:
    await db[TodoList].delete(pk=id)
    return None
