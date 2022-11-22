import typing
from strawberry.permission import BasePermission
from strawberry.types import Info
from starlette.requests import Request
from starlette.websockets import WebSocket
import os
from jose import jwt
from dotenv import load_dotenv

from infrastructure.auth.repository.repository import auth_repository
from domain.auth.entity.user import User

load_dotenv()
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITH = os.environ.get("JWT_ALGORITH")


def authenticate_header(request) -> (User | None):
    authorization = request.headers.get("Authorization")
    token = authorization.split()[-1]
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITH)
    user_id: str = payload.get("id")
    username: str = payload.get("sub")

    if username is None or user_id is None:
        return None

    user = auth_repository.authenticate(username)
    return user


class IsAuthenticated(BasePermission):
    """Check only if the token is valid"""

    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]
        if "Authorization" in request.headers:
            user = authenticate_header(request)
            if user is not None:
                return True
        else:
            self.message = "Token not found"
        return False


class IsAuthenticatedActive(BasePermission):
    """Check if the token is valid and that the user is active"""
    message = "User is not active"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]
        if "Authorization" in request.headers:
            user = authenticate_header(request)
            if user is not None:
                return user.is_active
        else:
            self.message = "Token not found"
        return False


class IsAuthenticatedSameUser(BasePermission):
    """Check if the token is valid and that the user is active"""
    message = "Invalid credentials for this user"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]
        if "Authorization" in request.headers:
            user = authenticate_header(request)

            if "userId" in kwargs:
                return kwargs.get('userId') == user.id
        else:
            self.message = "Token not found"
        return False
