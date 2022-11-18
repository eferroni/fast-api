from typing import TypedDict


class OutputGetUserDto(TypedDict):
    id: str
    username: str
    is_active: bool
