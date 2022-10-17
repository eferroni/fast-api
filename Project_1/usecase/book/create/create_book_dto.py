from typing import TypedDict


class InputCreateBookDto(TypedDict):
    title: str
    author: str


class OutputCreateBookDto(TypedDict):
    id: str
    title: str
    author: str

