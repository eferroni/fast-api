from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from domain.account.entity.user import User, UserProps
from domain.user.exceptions.user_exceptions import UserNotFound
from infrastructure.user.repository.dict.user_dictionary import USERS


class AccountRepositoryDict(AccountRepositoryInterface):
    def update(self, user: User) -> None:
        USERS[user.id]['username'] = user.username
        USERS[user.id]['email'] = user.email
        USERS[user.id]['first_name'] = user.first_name
        USERS[user.id]['last_name'] = user.last_name
        USERS[user.id]['hashed_password'] = user.hashed_password
        USERS[user.id]['is_active'] = user.is_active

    def find(self, user_id: str) -> User:
        if user_id not in USERS:
            raise UserNotFound
        user_item: dict = USERS[user_id]
        props: UserProps = {
            'id': user_id,
            'username': user_item['username'],
            'email': user_item['email'],
            'first_name': user_item['first_name'],
            'last_name': user_item['last_name'],
            'hashed_password': user_item['hashed_password'],
            'is_active': user_item['is_active']
        }
        user = User(props)
        return user

    def delete(self, user: User) -> None:
        del USERS[user.id]
