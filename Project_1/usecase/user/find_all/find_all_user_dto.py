from typing import TypedDict, Optional, Literal, List


class InputFindAllUserDto(TypedDict):
    username: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    page: int
    size: int
    order: Literal['username', 'email', 'first_name', 'last_name']


class User(TypedDict):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool


class OutputFindAllUserDto(TypedDict):
    users: List[User]
    total: int
    page: int
    size: int

