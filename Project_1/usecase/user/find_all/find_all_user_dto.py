from typing import TypedDict, Optional


class InputFindAllUserDto(TypedDict):
    id: Optional[str]


class OutputFindAllUserDto(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool

