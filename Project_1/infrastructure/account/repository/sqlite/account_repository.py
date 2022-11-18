from sqlalchemy import select, delete, update

from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from domain.account.entity.user import User, UserProps
from domain.user.exceptions.user_exceptions import UserNotFound
from infrastructure.__shared__.repository.sqlite.database import SessionLocal
import infrastructure.user.repository.sqlite.user_model as models


class AccountRepositorySqlite(AccountRepositoryInterface):
    def find(self, user_id: str) -> User:
        with SessionLocal() as s:
            query = s.execute(
                select(models.Users).where(models.Users.id == user_id)
            )
            user_item = query.scalar()
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
        with SessionLocal() as s:
            s.execute(
                update(models.Users).where(
                    models.Users.id == user.id
                ).values(
                    username=user.username,
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    hashed_password=user.hashed_password,
                    is_active=user.is_active,
                )
            )
            s.commit()

    def delete(self, user: User) -> None:
        with SessionLocal() as s:
            s.execute(
                delete(models.Users).where(models.Users.id == user.id)
            )
            s.commit()
