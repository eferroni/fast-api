import re

from domain.user.entity.user import User
from domain.user.repository.user_repository_interface import UserRepositoryInterface
from domain.user.exceptions.user_exceptions import UserNotFound
from infrastructure.__shared__.repository.mongo.database import get_database


class UserRepositoryMongo(UserRepositoryInterface):
    def __init__(self):
        self.db_name = get_database()
        self.collection = self.db_name['users']

    def count(self, username: str, email: str, first_name: str, last_name: str) -> int:
        query_filter = {}
        if username is not None:
            query_filter['username'] = re.compile(username, re.IGNORECASE)
        if email is not None:
            query_filter['email'] = re.compile(email, re.IGNORECASE)
        if first_name is not None:
            query_filter['first_name'] = re.compile(first_name, re.IGNORECASE)
        if last_name is not None:
            query_filter['last_name'] = re.compile(last_name, re.IGNORECASE)

        count = self.collection.count_documents(query_filter)
        return count

    def find(self, user_id: str) -> User:
        user_item = self.collection.find_one({'_id': user_id})
        if user_item is None:
            raise UserNotFound
        user = User(user_item.get('_id'), user_item.get('username'), user_item.get('email'),
                    user_item.get('first_name'), user_item.get('last_name'), None, user_item.get('is_active'))
        return user

    def find_all(self, username: str, email: str, first_name: str,
                 last_name: str, page: int, size: int, order: str) -> list[User]:
        query_filter = {}
        if username is not None:
            query_filter['username'] = re.compile(username, re.IGNORECASE)
        if email is not None:
            query_filter['email'] = re.compile(email, re.IGNORECASE)
        if first_name is not None:
            query_filter['first_name'] = re.compile(first_name, re.IGNORECASE)
        if last_name is not None:
            query_filter['last_name'] = re.compile(last_name, re.IGNORECASE)

        users = self.collection.find(query_filter).skip(((page-1)*size)).limit(size).sort(order)
        return [
            User(user_item.get('_id'), user_item.get('username'),
                 user_item.get('email'), user_item.get('first_name'),
                 user_item.get('last_name'), None,
                 user_item.get('is_active')) for user_item in users
        ]
