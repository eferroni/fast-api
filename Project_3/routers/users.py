import sys
sys.path.append("..")

from typing import Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi import Depends, status, APIRouter

import models
# from infrastructure.sqlite.database import engine, SessionLocal
from infrastructure.postgres.database import engine, SessionLocal
# from infrastructure.mysql.database import engine, SessionLocal
from exceptions.user_exceptions import UserNotFoundException
from .auth import get_current_user, get_password_hash, verify_password

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"description": "Not found"}})

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/")
def read_all_users(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    if user_id:
        return db.query(models.Users).filter(models.Users.id == user_id).all()
    return db.query(models.Users).all()


@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users)\
        .filter(models.Users.id == user_id)\
        .first()
    if user_model is not None:
        return user_model
    raise UserNotFoundException


@router.put("/password")
def update_user_password(user_verification: UserVerification,
                user_auth: dict = Depends(get_current_user),
                db: Session = Depends(get_db)):
    if user_auth is None:
        raise UserNotFoundException

    user_model = db.query(models.Users)\
        .filter(models.Users.id == user_auth.get("id"))\
        .first()

    if user_model is None:
        raise UserNotFoundException

    if user_verification.username != user_model.username \
            or not verify_password(user_verification.password, user_model.hashed_password):
        raise UserNotFoundException

    hash_password = get_password_hash(user_verification.new_password)
    user_model.hashed_password = hash_password

    db.add(user_model)
    db.commit()

    return {
        "status": 200,
        "transaction": "Successful"
    }


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise UserNotFoundException

    user_model = db.query(models.Users)\
        .filter(models.Users.id == user.get("id"))\
        .first()

    if user_model is None:
        raise UserNotFoundException

    db.delete(user_model)
    db.commit()
    return
