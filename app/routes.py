from fastapi import APIRouter, Depends, HTTPException
from ormdantic import Ormdantic
from starlette import status

from app import crud
from app.db import _init_db
from app.schema import TodoItem, TodoItemIn

router = APIRouter()


@router.post(
    "/todos",
    response_model=TodoItem,
    status_code=status.HTTP_201_CREATED,
    tags=["Todo List"],
)
async def create_todo_api(todo: TodoItemIn, database: Ormdantic = Depends(_init_db)):
    return await crud.create_todo(todo.title, todo.description, database)


@router.delete(
    "/todos/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Todo List"]
)
async def delete_todo_api(id: int, database: Ormdantic = Depends(_init_db)):
    if not await crud.exist(id, database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found"
        )
    await crud.delete_todo(id, database)
    return {"message": "Item deleted successfully"}
