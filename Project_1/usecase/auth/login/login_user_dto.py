from typing import TypedDict


class InputLoginUserDto(TypedDict):
    username: str
    password: str


class OutputLoginUserDto(TypedDict):
    token: str

