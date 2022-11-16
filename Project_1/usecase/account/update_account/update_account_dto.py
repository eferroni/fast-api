from typing import TypedDict


class InputUpdateAccountDto(TypedDict):
    id: str
    email: str
    first_name: str
    last_name: str


class OutputUpdateAccountDto(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool

