
from infrastructure.graphql.__shared__.schemas.page_info_schema import PageInfoSchema
from infrastructure.graphql.user.schemas.find.find_user_schema import FindUserSchema
from infrastructure.graphql.user.schemas.find_all.find_all_user_schema import (
    FindAllUserSchema, UserEdges, UserNode
)
from usecase.user.find.find_user_dto import OutputFindUserDto
from usecase.user.find_all.find_all_user_dto import OutputFindAllUserDto


class UserPresenter:
    @staticmethod
    def find_user_to_graphql_schema(data: OutputFindUserDto) -> FindUserSchema:
        return FindUserSchema(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            is_active=data.get('is_active')
        )

    @staticmethod
    def find_all_users_to_graphql_schema(data: OutputFindAllUserDto) -> FindAllUserSchema:
        return FindAllUserSchema(
            edges=[
                UserEdges(
                    node=UserNode(
                        id=user.get('id'),
                        username=user.get('username'),
                        email=user.get('email'),
                        first_name=user.get('first_name'),
                        last_name=user.get('last_name'),
                        is_active=user.get('is_active')
                    ),
                    cursor=user.get('id')
                ) for user in data.get('users')
            ],
            pageInfo=PageInfoSchema(
                totalCount=data.get('total'),
                page=data.get('page'),
                size=data.get('size'),
                hasPreviousPage=data.get('page') > 1,
                hasNextPage=data.get('total') > data.get('page')*data.get('size'),
                endCursor=data.get('users')[-1]['id']
            )
        )
