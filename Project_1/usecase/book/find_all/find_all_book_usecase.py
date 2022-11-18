from domain.book.repository.book_repository_interface import BookRepositoryInterface
from usecase.book.find_all.find_all_book_dto import OutputFindAllBookDto, InputFindAllBookDto


class FindAllBookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputFindAllBookDto) -> OutputFindAllBookDto:
        book_list = self.repository.find_all(
            title=input_dto.get("title"),
            author=input_dto.get("author"),
            page=input_dto.get("page"),
            size=input_dto.get("size"),
            order=input_dto.get("order")
        )
        total = self.repository.count(
            book_title=input_dto.get("title"),
            book_author=input_dto.get("author"),
        )
        return {
            'books': [
                {
                    "id": book_item.id,
                    "title": book_item.title,
                    "author": book_item.author
                } for book_item in book_list
            ],
            'total': total,
            'page': input_dto.get("page"),
            'size': input_dto.get("size")
        }
