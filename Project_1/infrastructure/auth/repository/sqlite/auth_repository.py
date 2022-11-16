from sqlalchemy.exc import IntegrityError

from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from domain.auth.repository.auth_repository_interface import AuthRepositoryInterface
from domain.auth.entity.user import User
from domain.user.exceptions.user_exceptions import UserAlreadyExist
from infrastructure.__shared__.repository.sqlite.database import SessionLocal
import infrastructure.user.repository.sqlite.user_model as models


class AuthRepositorySqlite(AuthRepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def find(self, username: str) -> bool:
        user_item = self.session.query(models.Users).filter(models.Users.username == username).first()
        if user_item is None:
            return False
        return True

    def create(self, user: User) -> None:
        try:
            user_model = models.Users()
            user_model.id = user.id
            user_model.username = user.username
            user_model.email = user.email
            user_model.first_name = user.first_name
            user_model.last_name = user.last_name
            user_model.hashed_password = user.hashed_password
            user_model.is_active = True

            self.session.add(user_model)
            self.commit()
        except IntegrityError:
            raise UserAlreadyExist('User Id already exist')

    def authenticate(self, username: str) -> User:
        user_item = self.session.query(models.Users).filter(models.Users.username == username).first()
        if user_item is None:
            raise AuthUnauthorizedException
        props = {
            'id': user_item.id,
            'username': user_item.username,
            'email': user_item.email,
            'first_name': user_item.first_name,
            'last_name': user_item.last_name,
            'hashed_password': user_item.hashed_password
        }
        user = User(props)
        return user
