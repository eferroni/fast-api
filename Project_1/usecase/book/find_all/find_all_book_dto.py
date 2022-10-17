from typing import TypedDict, Optional


class InputFindAllBookDto(TypedDict):
    id: Optional[str]


class OutputFindAllBookDto(TypedDict):
    id: str
    title: str
    author: str

