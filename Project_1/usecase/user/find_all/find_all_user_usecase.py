from domain.user.repository.user_repository_interface import UserRepositoryInterface
from usecase.user.find_all.find_all_user_dto import InputFindAllUserDto, OutputFindAllUserDto


class FindAllUserUseCase:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputFindAllUserDto) -> OutputFindAllUserDto:
        user_list = self.repository.find_all(
            username=input_dto.get("username"),
            email=input_dto.get("email"),
            first_name=input_dto.get("first_name"),
            last_name=input_dto.get("last_name"),
            page=input_dto.get("page"),
            size=input_dto.get("size"),
            order=input_dto.get("order")
        )
        total = self.repository.count(
            username=input_dto.get("username"),
            email=input_dto.get("email"),
            first_name=input_dto.get("first_name"),
            last_name=input_dto.get("last_name"),
        )
        return {
            'users': [
                {
                    "id": user_item.id,
                    "username": user_item.username,
                    "email": user_item.email,
                    "first_name": user_item.first_name,
                    "last_name": user_item.last_name,
                    "is_active": user_item.is_active
                } for user_item in user_list
            ],
            'total': total,
            'page': input_dto.get("page"),
            'size': input_dto.get("size")
        }
