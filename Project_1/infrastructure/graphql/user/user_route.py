from typing import Optional
from fastapi import APIRouter

from infrastructure.graphql.user.presenters.user_presenter import UserPresenter
from infrastructure.graphql.user.schemas.find.find_user_schema import FindUserSchema
from infrastructure.graphql.user.schemas.find_all.find_all_user_schema import FindAllUserSchema
from usecase.user.find.find_user_dto import InputFindUserDto, OutputFindUserDto
from usecase.user.find.find_user_usecase import FindUserUseCase
from usecase.user.find_all.find_all_user_dto import OutputFindAllUserDto, InputFindAllUserDto
from usecase.user.find_all.find_all_user_usecase import FindAllUserUseCase
from infrastructure.user.repository.repository import user_repository


async def find_all_users(username: Optional[str] = None,
                         email: Optional[str] = None,
                         first_name: Optional[str] = None,
                         last_name: Optional[str] = None,
                         page: int = 1,
                         size: int = 10,
                         order: str = 'username',
                         ) -> FindAllUserSchema:
    input_dto: InputFindAllUserDto = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'page': page,
        'size': size,
        'order': order
    }
    use_case = FindAllUserUseCase(user_repository)
    output_dto: OutputFindAllUserDto = use_case.execute(input_dto)
    return UserPresenter.find_all_users_to_graphql_schema(output_dto)


def find_user(user_id: str) -> FindUserSchema:
    input_dto: InputFindUserDto = {"id": user_id}
    output_dto: OutputFindUserDto = FindUserUseCase(user_repository).execute(input_dto)
    return UserPresenter.find_user_to_graphql_schema(output_dto)
