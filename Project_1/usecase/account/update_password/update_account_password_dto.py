from typing import TypedDict


class InputUpdateAccountPasswordDto(TypedDict):
    id: str
    username: str
    password: str
    new_password: str

