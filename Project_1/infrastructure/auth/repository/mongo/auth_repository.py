from pymongo.errors import DuplicateKeyError

from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from domain.auth.repository.auth_repository_interface import AuthRepositoryInterface
from domain.auth.entity.user import User
from domain.user.exceptions.user_exceptions import UserAlreadyExist
from infrastructure.__shared__.repository.mongo.database import get_database


class AuthRepositoryMongo(AuthRepositoryInterface):
    def __init__(self):
        self.db_name = get_database()
        self.collection = self.db_name['users']

    def active(self, user_id: str) -> bool:
        user_item = self.collection.find_one({'_id': user_id})
        if user_item is None:
            return False
        return user_item.get('is_active')

    def find(self, username: str) -> bool:
        user_item = self.collection.find_one({'username': username})
        if user_item is None:
            return False
        return True

    def create(self, user: User) -> None:
        try:
            user_item = {
                "_id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "hashed_password": user.hashed_password,
                "is_active": True,
            }

            self.collection.insert_one(user_item)

        except DuplicateKeyError:
            raise UserAlreadyExist('User Id already exist')

    def authenticate(self, username: str) -> User:
        user_item = self.collection.find_one({'username': username})
        if user_item is None:
            raise AuthUnauthorizedException
        props = {
            'id': user_item.get('_id'),
            'username': user_item.get('username'),
            'email': user_item.get('email'),
            'first_name': user_item.get('first_name'),
            'last_name': user_item.get('last_name'),
            'hashed_password': user_item.get('hashed_password')
        }
        user = User(props)
        return user
