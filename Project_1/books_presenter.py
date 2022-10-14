from abc import ABC, abstractmethod

from books_constants import BOOKS


class BookDTO:
    def __init__(self, book_title: str, book_author: str, book_id: str) -> None:
        self.id = book_id
        self.title = book_title
        self.author = book_author


class BookData(ABC):
    @abstractmethod
    def create(self, book_dto_input: BookDTO) -> BookDTO:
        pass

    @abstractmethod
    def get(self, book_dto_input: BookDTO) -> BookDTO:
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


class GetBookUseCase:
    def __init__(self, book_dto_input: BookDTO, book_data: BookData):
        self.book_dto_input = book_dto_input
        self.__validate()
        self.book_data = book_data

    def __validate(self) -> None:
        if not isinstance(self.book_dto_input.id, str):
            raise ValueError("The id must be a string")
        if self.book_dto_input.id == "":
            raise ValueError("The id must be passed")

    def get(self) -> BookDTO:
        return self.book_data.get(self.book_dto_input)


class BookDataDict(BookData):

    def create(self, book_dto_input: BookDTO) -> BookDTO:
        new_id = 1
        if len(BOOKS) > 0:
            new_id = int(list(BOOKS.keys())[-1].split('_')[-1]) + 1
        book_dto_input.id = f'book_{new_id}'
        BOOKS[f'book_{book_dto_input.id}'] = {'title': book_dto_input.title, 'author': book_dto_input.author}
        return book_dto_input

    def get(self, book_dto_input: BookDTO) -> BookDTO:
        book = BOOKS[book_dto_input.id]
        book_dto_input.title = book['title']
        book_dto_input.author = book['author']
        return book_dto_input


class BookPresenter:
    def __init__(self, book_dto_output: BookDTO):
        self.book_dto_output = book_dto_output

    def to_json(self):
        return {
            self.book_dto_output.id: {
                "title": self.book_dto_output.title,
                "author": self.book_dto_output.author
            }
        }
