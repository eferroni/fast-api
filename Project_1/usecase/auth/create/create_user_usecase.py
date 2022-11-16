import uuid

from domain.auth.entity.user import User, UserProps
from domain.auth.repository.auth_repository_interface import AuthRepositoryInterface
from domain.user.exceptions.user_exceptions import UserAlreadyExist
from usecase.auth.create.create_user_dto import InputCreateUserDto, OutputCreateUserDto


class CreateUserUseCase:
    def __init__(self, repository: AuthRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputCreateUserDto) -> OutputCreateUserDto:
        if self.repository.find(input_dto.get('username')):
            raise UserAlreadyExist("Username already taken")

        user_id = str(uuid.uuid4())
        user_props: UserProps = {
            "id": user_id,
            "username": input_dto.get('username'),
            "email": input_dto.get('email'),
            "first_name": input_dto.get('first_name'),
            "last_name": input_dto.get('last_name'),
            "hashed_password": ''
        }
        user = User(user_props)
        user.generate_hashed_password(input_dto.get('password'))

        self.repository.create(user)
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
