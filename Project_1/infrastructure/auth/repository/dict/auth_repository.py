from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from domain.auth.repository.auth_repository_interface import AuthRepositoryInterface
from domain.auth.entity.user import User
from infrastructure.user.repository.dict.user_dictionary import USERS
from domain.user.exceptions.user_exceptions import UserAlreadyExist


class AuthRepositoryDict(AuthRepositoryInterface):
    def active(self, user_id: str) -> bool:
        if user_id not in USERS:
            return False
        return USERS[user_id]['is_active']

    def find(self, username: str) -> bool:
        for user_id in USERS:
            if USERS[user_id]['username'] == username:
                return True
        return False

    def create(self, user: User) -> None:
        if user.id in USERS:
            raise UserAlreadyExist('User Id already exist')
        for user_item in USERS.keys():
            if USERS[user_item]['username'] == user.username:
                raise UserAlreadyExist('Username already taken')
        USERS[user.id] = {'username': user.username, 'email': user.email, 'first_name': user.first_name,
                          'last_name': user.last_name, 'hashed_password': user.hashed_password,
                          'is_active': True}

    def authenticate(self, username: str) -> User:
        for user_item in USERS.keys():
            if USERS[user_item]['username'] == username:
                props = {
                    'id': user_item,
                    'username': USERS[user_item]['username'],
                    'email': USERS[user_item]['email'],
                    'first_name': USERS[user_item]['first_name'],
                    'last_name': USERS[user_item]['last_name'],
                    'hashed_password': USERS[user_item]['hashed_password']
                }
                user = User(props)
                return user
        raise AuthUnauthorizedException
