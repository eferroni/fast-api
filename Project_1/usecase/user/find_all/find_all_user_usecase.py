from domain.user.repository.user_repository_interface import UserRepositoryInterface
from usecase.user.find_all.find_all_user_dto import InputFindAllUserDto, OutputFindAllUserDto


class FindAllUserUseCase:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputFindAllUserDto) -> list[OutputFindAllUserDto]:
        output = list()
        user_list = self.repository.find_all(input_dto.get("id", None))
        for user_item in user_list:
            output.append(
                {
                    "id": user_item.id,
                    "username": user_item.username,
                    "email": user_item.email,
                    "first_name": user_item.first_name,
                    "last_name": user_item.last_name,
                    "is_active": user_item.is_active
                }
            )
        return output
