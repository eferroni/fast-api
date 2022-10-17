from typing import TypedDict


class InputFindBookDto(TypedDict):
    id: str


class OutputFindBookDto(TypedDict):
    id: str
    title: str
    author: str

