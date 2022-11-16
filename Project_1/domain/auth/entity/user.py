from typing import TypedDict

from domain.password.domain.password import Password


class UserProps(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    hashed_password: str


class User(Password):
    def __init__(self, props: UserProps):
        self._id = props.get('id')
        self._username = props.get('username')
        self._email = props.get('email')
        self._first_name = props.get('first_name')
        self._last_name = props.get('last_name')
        super().__init__(props.get('hashed_password'))

    @property
    def id(self) -> str:
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name
