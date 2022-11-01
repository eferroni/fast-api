from domain.book.repository.book_repository_interface import BookRepositoryInterface
from usecase.book.find_all.find_all_book_dto import OutputFindAllBookDto, InputFindAllBookDto


class FindAllBookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputFindAllBookDto) -> list[OutputFindAllBookDto]:
        output = list()
        book_list = self.repository.find_all(input_dto.get("id", None))
        for book_item in book_list:
            output.append(
                {
                    "id": book_item.id,
                    "title": book_item.title,
                    "author": book_item.author
                }
            )
        return output
