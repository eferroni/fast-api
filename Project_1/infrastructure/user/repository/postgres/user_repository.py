import re

from sqlalchemy import select, func

from domain.user.entity.user import User
from domain.user.repository.user_repository_interface import UserRepositoryInterface
from domain.user.exceptions.user_exceptions import UserNotFound
from infrastructure.__shared__.repository.postgres.database import SessionLocal
import infrastructure.user.repository.postgres.user_model as models


class UserRepositoryPostgres(UserRepositoryInterface):
    def count(self, username: str, email: str, first_name: str, last_name: str) -> int:
        with SessionLocal() as s:
            query_filter = list()
            if username is not None:
                query_filter.append(models.Users.username.ilike(f'%{username}%'))
            if email is not None:
                query_filter.append(models.Users.email.ilike(f'%{email}%'))
            if first_name is not None:
                query_filter.append(models.Users.first_name.ilike(f'%{first_name}%'))
            if last_name is not None:
                query_filter.append(models.Users.last_name.ilike(f'%{last_name}%'))
            count = s.execute(
                select(func.count()).select_from(models.Users)
                .where(*query_filter)
            ).scalar()
            return count

    def find(self, user_id: str) -> User:
        with SessionLocal() as s:
            query = s.execute(
                select(models.Users).where(models.Users.id == user_id)
            )
            user_item = query.scalar()
        if user_item is None:
            raise UserNotFound
        user = User(user_item.id, user_item.username, user_item.email, user_item.first_name,
                    user_item.last_name, None, user_item.is_active)
        return user

    def find_all(self, username: str, email: str, first_name: str,
                 last_name: str, page: int, size: int, order: str) -> list[User]:
        with SessionLocal() as s:
            query_filter = list()
            if username is not None:
                query_filter.append(models.Users.username.ilike(f'%{username}%'))
            if email is not None:
                query_filter.append(models.Users.email.ilike(f'%{email}%'))
            if first_name is not None:
                query_filter.append(models.Users.first_name.ilike(f'%{first_name}%'))
            if last_name is not None:
                query_filter.append(models.Users.last_name.ilike(f'%{last_name}%'))

            query = s.execute(
                select(models.Users).where(*query_filter)
                .offset(((page - 1) * size)).limit(size).order_by(order)
            )
            users = query.scalars().all()

        return [
            User(user_item.id, user_item.username, user_item.email, user_item.first_name,
                 user_item.last_name, None, user_item.is_active) for user_item in users
        ]
