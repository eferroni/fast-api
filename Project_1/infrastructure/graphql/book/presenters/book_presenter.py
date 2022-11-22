from typing import List

from infrastructure.graphql.__shared__.schemas.page_info_schema import PageInfoSchema
from infrastructure.graphql.book.schemas.create.create_book_schema import CreateBookSchema
from infrastructure.graphql.book.schemas.delete.delete_book_schema import DeleteBookSchema
from infrastructure.graphql.book.schemas.find.find_book_schema import FindBookSchema
from infrastructure.graphql.book.schemas.find_all.find_all_book_schema import (
    FindAllBookSchema, Edges, Node)
from infrastructure.graphql.book.schemas.update.update_book_schema import UpdateBookSchema
from usecase.book.create.create_book_dto import OutputCreateBookDto
from usecase.book.delete.delete_book_dto import OutputDeleteBookDto
from usecase.book.find.find_book_dto import OutputFindBookDto
from usecase.book.find_all.find_all_book_dto import OutputFindAllBookDto
from usecase.book.update.update_book_dto import OutputUpdateBookDto


class BookPresenter:
    @staticmethod
    def find_book_to_graphql_schema(data: OutputFindBookDto) -> FindBookSchema:
        return FindBookSchema(
            id=data.get('id'),
            title=data.get('title'),
            author=data.get('author'),
        )

    @staticmethod
    def find_all_books_to_graphql_schema(data: OutputFindAllBookDto) -> FindAllBookSchema:
        return FindAllBookSchema(
            edges=[
                Edges(
                    node=Node(
                        id=book.get('id'),
                        title=book.get('title'),
                        author=book.get('author'),
                    ),
                    cursor=book.get('id')
                ) for book in data.get('books')
            ],
            pageInfo=PageInfoSchema(
                totalCount=data.get('total'),
                page=data.get('page'),
                size=data.get('size'),
                hasPreviousPage=data.get('page') > 1,
                hasNextPage=data.get('total') > data.get('page')*data.get('size'),
                endCursor=data.get('books')[-1]['id']
            )
        )

    @staticmethod
    def add_book_to_graphql_schema(data: OutputCreateBookDto) -> CreateBookSchema:
        return CreateBookSchema(
            id=data.get('id'),
            title=data.get('title'),
            author=data.get('author'),
        )

    @staticmethod
    def update_book_to_graphql_schema(data: OutputUpdateBookDto) -> UpdateBookSchema:
        return UpdateBookSchema(
            id=data.get('id'),
            title=data.get('title'),
            author=data.get('author'),
        )

    @staticmethod
    def delete_book_to_graphql_schema(data: OutputDeleteBookDto) -> DeleteBookSchema:
        return DeleteBookSchema(
            message=data.get('message'),
        )
