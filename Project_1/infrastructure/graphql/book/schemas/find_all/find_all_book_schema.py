import strawberry
from typing import List

from infrastructure.graphql.__shared__.schemas.page_info_schema import PageInfoSchema


@strawberry.type
class Node:
    id: str
    title: str
    author: str


@strawberry.type
class Edges:
    node: Node
    cursor: str


@strawberry.type
class FindAllBookSchema:
    edges: List[Edges]
    pageInfo: PageInfoSchema
