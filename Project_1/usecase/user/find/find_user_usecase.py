from domain.user.repository.user_repository_interface import UserRepositoryInterface
from usecase.user.find.find_user_dto import InputFindUserDto, OutputFindUserDto


class FindUserUseCase:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputFindUserDto) -> OutputFindUserDto:
        user = self.repository.find(input_dto['id'])
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_active": user.is_active
        }
