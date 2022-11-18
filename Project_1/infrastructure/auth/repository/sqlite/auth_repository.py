from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from domain.auth.repository.auth_repository_interface import AuthRepositoryInterface
from domain.auth.entity.user import User
from domain.user.exceptions.user_exceptions import UserAlreadyExist
from infrastructure.__shared__.repository.sqlite.database import SessionLocal
import infrastructure.user.repository.sqlite.user_model as models


class AuthRepositorySqlite(AuthRepositoryInterface):
    def exist_username(self, username: str) -> bool:
        with SessionLocal() as s:
            query = s.execute(
                select(models.Users).where(models.Users.username == username)
            )
            user_item = query.scalar()
        if user_item is None:
            return False
        return True

    def create(self, user: User) -> None:
        try:
            with SessionLocal() as s:
                user_model = models.Users()
                user_model.id = user.id
                user_model.username = user.username
                user_model.email = user.email
                user_model.first_name = user.first_name
                user_model.last_name = user.last_name
                user_model.hashed_password = user.hashed_password
                user_model.is_active = True

                s.add(user_model)
                s.commit()
        except IntegrityError:
            raise UserAlreadyExist('User already exist')

    def authenticate(self, username: str) -> User:
        with SessionLocal() as s:
            query = s.execute(
                select(models.Users).where(models.Users.username == username)
            )
            user_item = query.scalar()
        if user_item is None:
            raise AuthUnauthorizedException
        props = {
            'id': user_item.id,
            'username': user_item.username,
            'email': user_item.email,
            'first_name': user_item.first_name,
            'last_name': user_item.last_name,
            'hashed_password': user_item.hashed_password,
            'is_active': user_item.is_active
        }
        user = User(props)
        return user
