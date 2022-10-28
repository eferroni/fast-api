from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError
import models
# from sqlite.database import SessionLocal, engine
# from postgres.database import SessionLocal, engine
from mysql.database import SessionLocal, engine
from exceptions.user_exceptions import UserNotFoundException
from exceptions.auth_exceptions import AuthUnauthorizedException, AuthTokenException

SECRET_KEY = "KdskjdsLKJSdILDJEdSdae93d83uqw"
ALGORITH = "HS256"


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str

    class Config():
        schema_extra = {
            "example": {
                "username": "eferroni",
                "email": "eferroni@email.com",
                "first_name": "Eduardo",
                "last_name": "Ferroni",
                "password": "password"
            }
    }


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password: str):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None):
    encode = {
        "sub": username,
        "id": user_id
    }
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITH)


def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITH)
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise UserNotFoundException
        return {"username": username, "id": user_id}
    except JWTError:
        raise AuthUnauthorizedException


@app.post("/users/create/", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser,  db: Session = Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.email = user.email
    create_user_model.username = user.username
    create_user_model.first_name = user.first_name
    create_user_model.last_name = user.last_name

    hash_password = get_password_hash(user.password)
    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()

    return create_user_model


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise AuthTokenException
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username, user.id, expires_delta=token_expires)
    return {"token": token}
