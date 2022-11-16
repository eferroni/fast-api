from typing import TypedDict


class InputCreateUserDto(TypedDict):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str


class OutputCreateUserDto(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str

