from domain.user.entity.user import User
from domain.user.repository.user_repository_interface import UserRepositoryInterface
from infrastructure.user.repository.dict.user_dictionary import USERS
from domain.user.exceptions.user_exceptions import UserNotFound


class UserRepositoryDict(UserRepositoryInterface):
    def find(self, user_id: str) -> User:
        if user_id not in USERS:
            raise UserNotFound
        user_item = USERS[user_id]
        user = User(user_id, user_item['username'], user_item['email'], user_item['first_name'],
                    user_item['last_name'], None, user_item['is_active'])
        return user

    def find_all(self, user_id: str = None) -> list[User]:
        user_list = list()
        for user_item in USERS.keys():
            append = True
            if user_id is not None and user_item != user_id:
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

        return user_list
