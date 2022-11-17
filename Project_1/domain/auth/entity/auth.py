import os
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from domain.auth.entity.user import User
from domain.user.exceptions.user_exceptions import UserNotFound, UserInactive
from usecase.auth.get.get_user_dto import OutputGetUserDto
from infrastructure.auth.repository.repository import auth_repository

load_dotenv()
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITH = os.environ.get("JWT_ALGORITH")
JWT_EXPIRE_MINUTES = float(os.environ.get("JWT_EXPIRE_MINUTES"))

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


class Auth:
    def __init__(self, user: User):
        self._user = user

    def create_access_token(self, expires_delta: Optional[timedelta] = None):
        encode = {
            "id": self._user.id,
            "sub": self._user.username
        }
        if expires_delta is not None:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
        encode.update({"exp": expire})
        return jwt.encode(encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITH)

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_bearer)) -> OutputGetUserDto:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITH)
            user_id: str = payload.get("id")
            username: str = payload.get("sub")
            if username is None or user_id is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User not found",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            if auth_repository.active(user_id) is False:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User not found/inactive",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            return {"id": user_id, "username": username }
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )


