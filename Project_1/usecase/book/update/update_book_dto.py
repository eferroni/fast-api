from typing import TypedDict


class InputUpdateBookDto(TypedDict):
    id: str
    title: str
    author: str


class OutputUpdateBookDto(TypedDict):
    id: str
    title: str
    author: str

