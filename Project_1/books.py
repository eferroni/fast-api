from typing import Optional

from fastapi import FastAPI
from enum import Enum

from books_constants import BOOKS
from books_presenter import BookDTO, BookDataDict, CreateBookUseCase, BookPreseter

app = FastAPI()


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def fetch_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}
    return {"Direction": direction_name, "sub": "Right"}


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My Favorite one"}


@app.get("/{book_name}")
async def fetch_book(book_name: str):
    return BOOKS[book_name]


@app.get("/book/")
async def fetch_book_with_query_params(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title: str, book_author: str):
    input_dto = BookDTO(book_title, book_author)
    book_data = BookDataDict()
    output_dto = CreateBookUseCase(input_dto, book_data).create()
    json_result = BookPreseter(output_dto).to_json()
    return json_result


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    new_book_info = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = new_book_info
    return new_book_info


@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'


@app.delete("/book/")
async def delete_book_with_query_params(book_name: str):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'
