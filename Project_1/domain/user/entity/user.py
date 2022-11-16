from domain.user.exceptions.user_exceptions import UserValueError


class User:
    _id: str
    _username: str
    _email: str
    _first_name: str
    _last_name: str
    _hashed_password: str
    _is_active: bool

    def __init__(self, id: str, username: str, email: str, first_name: str,
                 last_name: str, hashed_password: str = None, is_active: bool = True):
        self._id = id
        self._username = username
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._hashed_password = hashed_password
        self._is_active = is_active
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
    def hashed_password(self) -> str:
        return self._hashed_password

    @property
    def is_active(self) -> bool:
        return self._is_active

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


