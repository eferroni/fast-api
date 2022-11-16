from sqlalchemy.exc import IntegrityError

from domain.user.entity.user import User
from domain.user.repository.user_repository_interface import UserRepositoryInterface
from domain.user.exceptions.user_exceptions import UserNotFound, UserAlreadyExist
from infrastructure.__shared__.repository.sqlite.database import SessionLocal
import infrastructure.user.repository.sqlite.user_model as models


class UserRepositorySqlite(UserRepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def find(self, user_id: str) -> User:
        user_item = self.session.query(models.Users).filter(models.Users.id == user_id).first()
        if user_item is None:
            raise UserNotFound
        user = User(user_item.id, user_item.username, user_item.email, user_item.first_name,
                    user_item.last_name, None, user_item.is_active)
        return user

    def find_all(self, user_id: str = None) -> list[User]:
        if user_id is None:
            users = self.session.query(models.Users).all()
        else:
            users = self.session.query(models.Users).filter(models.Users.id == user_id).all()
        user_list = list()
        for user_item in users:
            user = User(user_item.id, user_item.username, user_item.email, user_item.first_name,
                        user_item.last_name, None, user_item.is_active)
            user_list.append(user)
        return user_list
