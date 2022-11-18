import typing
import strawberry

from infrastructure.graphql.book import (
    BookSchema, find_all_books, find_book, add_book
)


@strawberry.type
class Query:
    books: typing.List[BookSchema] = strawberry.field(resolver=find_all_books)
    book: BookSchema = strawberry.field(resolver=find_book)


@strawberry.type
class Mutation:
    add_book: typing.List[BookSchema] = strawberry.field(resolver=add_book)


schema = strawberry.Schema(query=Query, mutation=Mutation)
