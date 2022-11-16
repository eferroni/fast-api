from typing import TypedDict


class InputFindUserDto(TypedDict):
    id: str


class OutputFindUserDto(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool

