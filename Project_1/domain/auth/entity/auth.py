import os
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from domain.auth.entity.user import User
from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
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


async def get_current_user(token: str = Depends(oauth2_bearer)) -> OutputGetUserDto:
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

        user = auth_repository.authenticate(username)

        return {"id": user.id, "username": user.username, "is_active":  user.is_active}
    except (AuthUnauthorizedException, ExpiredSignatureError, JWTError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_active_user(current_user: dict = Depends(get_current_user)):
    if current_user.get('is_active') is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user
