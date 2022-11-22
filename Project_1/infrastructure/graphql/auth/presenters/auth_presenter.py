from infrastructure.graphql.auth.schemas.create.create_user_schema import CreateUserSchema
from infrastructure.graphql.auth.schemas.login.login_schema import LoginSchema
from usecase.auth.create.create_user_dto import OutputCreateUserDto
from usecase.auth.login.login_user_dto import OutputLoginUserDto


class AuthPresenter:
    @staticmethod
    def create_user_to_graphql_schema(data: OutputCreateUserDto) -> CreateUserSchema:
        return CreateUserSchema(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
        )

    @staticmethod
    def login_to_graphql_schema(data: OutputLoginUserDto) -> LoginSchema:
        return LoginSchema(
            access_token=data.get('access_token'),
            token_type=data.get('token_type'),
        )

