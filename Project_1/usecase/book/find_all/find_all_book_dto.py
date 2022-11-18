from typing import TypedDict, Optional, List, Literal


class InputFindAllBookDto(TypedDict):
    title: Optional[str]
    author: Optional[str]
    page: int
    size: int
    order: Literal['title', 'author']


class BookDto(TypedDict):
    id: str
    title: str
    author: str


class OutputFindAllBookDto(TypedDict):
    books: List[BookDto]
    total: int
    page: int
    size: int


