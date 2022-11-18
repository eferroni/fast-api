import collections

from domain.user.entity.user import User
from domain.user.repository.user_repository_interface import UserRepositoryInterface
from infrastructure.user.repository.dict.user_dictionary import USERS
from domain.user.exceptions.user_exceptions import UserNotFound


class UserRepositoryDict(UserRepositoryInterface):
    def count(self, username: str, email: str, first_name: str, last_name: str) -> int:
        counter = 0
        for user_item in USERS.keys():
            append = True
            if username is not None and username.lower() not in USERS[user_item]['username'].lower():
                append = False
            if email is not None and email.lower() not in USERS[user_item]['email'].lower():
                append = False
            if first_name is not None and first_name.lower() not in USERS[user_item]['first_name'].lower():
                append = False
            if last_name is not None and last_name.lower() not in USERS[user_item]['last_name'].lower():
                append = False
            if append is True:
                counter += 1
        return counter

    def find(self, user_id: str) -> User:
        if user_id not in USERS:
            raise UserNotFound
        user_item = USERS[user_id]
        user = User(user_id, user_item['username'], user_item['email'], user_item['first_name'],
                    user_item['last_name'], None, user_item['is_active'])
        return user

    def find_all(self, username: str, email: str, first_name: str,
                 last_name: str, page: int, size: int, order: str) -> list[User]:
        result = collections.OrderedDict(sorted(USERS.items(), key=lambda t: t[1][order]))

        user_list = list()
        for user_item in result.keys():
            append = True
            if username is not None and username.lower() not in result[user_item]['username'].lower():
                append = False
            if email is not None and email.lower() not in result[user_item]['email'].lower():
                append = False
            if first_name is not None and first_name.lower() not in result[user_item]['first_name'].lower():
                append = False
            if last_name is not None and last_name.lower() not in result[user_item]['last_name'].lower():
                append = False
            if append is True:
                user = User(user_item,
                            USERS[user_item]['username'],
                            USERS[user_item]['email'],
                            USERS[user_item]['first_name'],
                            USERS[user_item]['last_name'],
                            None,
                            USERS[user_item]['is_active'])
                user_list.append(user)
        return user_list[((page-1)*size):(page * size)]
