from abc import ABC, abstractmethod

from books_constants import BOOKS


class BookDTO:
    def __init__(self, book_title: str, book_author: str, book_id=0) -> None:
        self.id = book_id
        self.title = book_title
        self.author = book_author


class BookData(ABC):
    @abstractmethod
    def create(self, book_dto_input: BookDTO) -> BookDTO:
        pass


class CreateBookUseCase:
    def __init__(self, book_dto_input: BookDTO, book_data: BookData):
        self.book_dto_input = book_dto_input
        self.__validate()
        self.book_data = book_data

    def __validate(self) -> None:
        if not isinstance(self.book_dto_input.title, str):
            raise ValueError("The title must be a string")
        if self.book_dto_input.title == "":
            raise ValueError("The title must be passed")
        if not isinstance(self.book_dto_input.author, str):
            raise ValueError("The author must be a string")
        if self.book_dto_input.author == "":
            raise ValueError("The author must be passed")

    def create(self) -> BookDTO:
        return self.book_data.create(self.book_dto_input)


class BookDataDict(BookData):

    def create(self, book_dto_input: BookDTO) -> BookDTO:
        if len(BOOKS) > 0:
            book_dto_input.id = int(list(BOOKS.keys())[-1].split('_')[-1]) + 1
        BOOKS[f'book_{book_dto_input.id}'] = {'title': book_dto_input.title, 'author': book_dto_input.author}
        return book_dto_input


class BookPreseter:
    def __init__(self, book_dto_output: BookDTO):
        self.book_dto_output = book_dto_output

    def to_json(self):
        return {
            f'book_{self.book_dto_output.id}': {
                "title": self.book_dto_output.title,
                "author": self.book_dto_output.author
            }
        }
