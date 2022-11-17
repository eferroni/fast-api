from typing import TypedDict


class InputLoginUserDto(TypedDict):
    username: str
    password: str


class OutputLoginUserDto(TypedDict):
    access_token: str
    token_type: str

