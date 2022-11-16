from sqlalchemy.exc import IntegrityError

from domain.account.entity.user import User, UserProps

from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from domain.user.exceptions.user_exceptions import UserAlreadyExist, UserNotFound
from infrastructure.__shared__.repository.postgres.database import SessionLocal
import infrastructure.user.repository.postgres.user_model as models


class AccountRepositoryPostgres(AccountRepositoryInterface):
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
        props: UserProps = {
            'id': user_id,
            'username': user_item.username,
            'email': user_item.email,
            'first_name': user_item.first_name,
            'last_name': user_item.last_name,
            'hashed_password': user_item.hashed_password,
            'is_active': user_item.is_active
        }
        user = User(props)
        return user

    def update(self, user: User) -> None:
        try:
            self.session.query(models.Users).filter(models.Users.id == user.id).update(
                {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "hashed_password": user.hashed_password,
                    "is_active": user.is_active
                }
            )
            self.commit()
        except IntegrityError:
            raise UserAlreadyExist('Username already taken')

    def delete(self, user: User) -> None:
        self.session.query(models.Users).filter(models.Users.id == user.id).delete()
        self.commit()
