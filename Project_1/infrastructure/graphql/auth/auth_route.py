from infrastructure.graphql.auth.presenters.auth_presenter import AuthPresenter
from infrastructure.graphql.auth.schemas.create.create_user_schema import CreateUserSchema
from infrastructure.graphql.auth.schemas.login.login_schema import LoginSchema
from usecase.auth.create.create_user_dto import InputCreateUserDto, OutputCreateUserDto
from usecase.auth.create.create_user_usecase import CreateUserUseCase
from usecase.auth.login.login_user_dto import InputLoginUserDto, OutputLoginUserDto
from usecase.auth.login.login_user_usecase import LoginUserUseCase
from infrastructure.auth.repository.repository import auth_repository


def create_user(username: str, email: str, first_name: str,
                last_name: str, password: str) -> CreateUserSchema:
    input_dto: InputCreateUserDto = {"username": username,
                                     "email": email,
                                     "first_name": first_name,
                                     "last_name": last_name,
                                     "password": password}
    output_dto: OutputCreateUserDto = CreateUserUseCase(auth_repository).execute(input_dto)
    return AuthPresenter.create_user_to_graphql_schema(output_dto)


def login(username: str, password: str) -> LoginSchema:
    input_dto: InputLoginUserDto = {"username": username,
                                    "password": password}
    output_dto: OutputLoginUserDto = LoginUserUseCase(auth_repository).execute(input_dto)
    return AuthPresenter.login_to_graphql_schema(output_dto)
