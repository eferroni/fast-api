from typing import TypedDict

from domain.password.domain.password import Password
from domain.user.exceptions.user_exceptions import UserValueError


class UserProps(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool


class User(Password):
    def __init__(self, props: UserProps):
        self._id = props.get('id')
        self._username = props.get('username')
        self._email = props.get('email')
        self._first_name = props.get('first_name')
        self._last_name = props.get('last_name')
        self._hashed_password = props.get('hashed_password')
        self._is_active = props.get('is_active')
        super().__init__(props.get('hashed_password'))
        self.validate()

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

    @property
    def is_active(self) -> bool:
        return self._is_active

    def activate(self) -> None:
        self._is_active = True
        self.validate()

    def deactivate(self) -> None:
        self._is_active = False
        self.validate()

    def change_email(self, new_email: str) -> None:
        self._email = new_email
        self.validate()

    def change_first_name(self, new_first_name: str) -> None:
        self._first_name = new_first_name
        self.validate()

    def change_last_name(self, new_last_name: str) -> None:
        self._last_name = new_last_name
        self.validate()

    def validate(self) -> None:
        if self._id == "":
            raise UserValueError("Id is required")
        if self._username == "":
            raise UserValueError("Username is required")
        if self._email == "":
            raise UserValueError("Email is required")
        if self._first_name == "":
            raise UserValueError("First Name is required")
        if self._last_name == "":
            raise UserValueError("Last Name is required")
        if self._hashed_password == "":
            raise UserValueError("Hashed Password is required")
        if self._is_active is None:
            raise UserValueError("Is Active is required")