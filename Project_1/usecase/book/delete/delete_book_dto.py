from typing import TypedDict


class InputDeleteBookDto(TypedDict):
    id: str


class OutputDeleteBookDto(TypedDict):
    message: str

