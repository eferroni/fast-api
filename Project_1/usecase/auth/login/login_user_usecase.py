from domain.auth.entity.auth import Auth
from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from domain.auth.repository.auth_repository_interface import AuthRepositoryInterface
from usecase.auth.login.login_user_dto import InputLoginUserDto, OutputLoginUserDto


class LoginUserUseCase:
    def __init__(self, repository: AuthRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputLoginUserDto) -> OutputLoginUserDto:
        user = self.repository.authenticate(input_dto.get('username'))
        if user.verify_password(input_dto.get('password')) is False:
            raise AuthUnauthorizedException

        auth = Auth(user)
        token = auth.create_access_token()
        return {
            "token": token,
        }
