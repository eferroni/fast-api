from pymongo.errors import DuplicateKeyError

from domain.account.entity.user import User, UserProps
from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from domain.user.exceptions.user_exceptions import UserAlreadyExist, UserNotFound
from infrastructure.__shared__.repository.mongo.database import get_database


class AccountRepositoryMongo(AccountRepositoryInterface):
    def __init__(self):
        self.db_name = get_database()
        self.collection = self.db_name['users']

    def find(self, user_id: str) -> User:
        user_item = self.collection.find_one({'_id': user_id})
        if user_id is None:
            raise UserNotFound
        props: UserProps = {
            'id': user_item.get('_id'),
            'username': user_item.get('username'),
            'email': user_item.get('email'),
            'first_name': user_item.get('first_name'),
            'last_name': user_item.get('last_name'),
            'hashed_password': user_item.get('hashed_password'),
            'is_active': user_item.get('is_active')
        }
        user = User(props)
        return user

    def update(self, user: User) -> None:
        try:
            self.collection.update_one({'_id': user.id}, {'$set': {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "hashed_password": user.hashed_password,
                "is_active": user.is_active,
            }})
        except DuplicateKeyError:
            raise UserAlreadyExist('Username already taken')

    def delete(self, user: User) -> None:
        self.collection.delete_one({'_id': user.id})
