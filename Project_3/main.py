from typing import Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, status

import models
# from sqlite.database import engine, SessionLocal
from postgres.database import engine, SessionLocal
from exceptions.todo_exceptions import TodoNotFoundException
from auth import get_current_user
from exceptions.user_exceptions import UserNotFoundException

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="Priority must be between 1 and 5")
    complete: bool


@app.get("/todos/")
def read_all_todos(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get('/todos/user')
def read_all_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise UserNotFoundException
    return db.query(models.Todos).filter(models.Todos.owner_id == user.get("id")).all()


@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise UserNotFoundException
    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get("id"))\
        .first()
    if todo_model is not None:
        return todo_model
    raise TodoNotFoundException


@app.post("/todos/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise UserNotFoundException
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    db.add(todo_model)
    db.commit()

    return {
        "status": 201,
        "transaction": "Successful"
    }


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise UserNotFoundException

    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get("id"))\
        .first()

    if todo_model is None:
        raise TodoNotFoundException

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return {
        "status": 200,
        "transaction": "Successful"
    }


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise UserNotFoundException

    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get("id"))\
        .first()

    if todo_model is None:
        raise TodoNotFoundException

    db.delete(todo_model)
    db.commit()
    return
