from domain.user.entity.user import User
from domain.user.repository.user_repository_interface import UserRepositoryInterface
from domain.user.exceptions.user_exceptions import UserNotFound, UserAlreadyExist
from infrastructure.__shared__.repository.mongo.database import get_database


class UserRepositoryMongo(UserRepositoryInterface):
    def __init__(self):
        self.db_name = get_database()
        self.collection = self.db_name['users']

    def find(self, user_id: str) -> User:
        user_item = self.collection.find_one({'_id': user_id})
        if user_item is None:
            raise UserNotFound
        user = User(user_item.get('_id'), user_item.get('username'), user_item.get('email'),
                    user_item.get('first_name'), user_item.get('last_name'), None, user_item.get('is_active'))
        return user

    def find_all(self, user_id: str = None) -> list[User]:
        if user_id is None:
            users = self.collection.find()
        else:
            users = self.collection.find({'_id': user_id})
        user_list = list()
        for user_item in users:
            user = User(user_item.get('_id'), user_item.get('username'), user_item.get('email'),
                        user_item.get('first_name'), user_item.get('last_name'), None, user_item.get('is_active'))
            user_list.append(user)
        return user_list
