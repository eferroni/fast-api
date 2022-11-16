import os
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from domain.auth.entity.user import User
from domain.auth.exceptions.auth_exceptions import AuthTokenException
from domain.user.exceptions.user_exceptions import UserNotFound
from usecase.auth.get.get_user_dto import OutputGetUserDto

load_dotenv()
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITH = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


class Auth:
    def __init__(self, user: User):
        self._user = user

    def create_access_token(self, expires_delta: Optional[timedelta] = None):
        encode = {
            "id": self._user.id,
            "username": self._user.username
        }
        if expires_delta is not None:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        encode.update({"exp": expire})
        return jwt.encode(encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITH)

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_bearer)) -> OutputGetUserDto:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITH)
            user_id: str = payload.get("id")
            username: str = payload.get("username")
            if username is None or user_id is None:
                raise UserNotFound
            return {"id": user_id, "username": username, }
        except JWTError:
            raise AuthTokenException


