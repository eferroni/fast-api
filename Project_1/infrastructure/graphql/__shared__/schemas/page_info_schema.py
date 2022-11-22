import strawberry


@strawberry.type
class PageInfoSchema:
    totalCount: int
    page: int
    size: int
    hasPreviousPage: bool
    hasNextPage: bool
    endCursor: str
