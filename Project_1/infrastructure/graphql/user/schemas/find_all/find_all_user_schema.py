import strawberry
from typing import List

from infrastructure.graphql.__shared__.schemas.page_info_schema import PageInfoSchema


@strawberry.type
class UserNode:
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool


@strawberry.type
class UserEdges:
    node: UserNode
    cursor: str


@strawberry.type
class FindAllUserSchema:
    edges: List[UserEdges]
    pageInfo: PageInfoSchema
