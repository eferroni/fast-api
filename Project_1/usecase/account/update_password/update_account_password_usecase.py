from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from domain.user.exceptions.user_exceptions import UserNotFound

from usecase.account.update_password.update_account_password_dto import InputUpdateAccountPasswordDto


class UpdateAccountPasswordUseCase:
    def __init__(self, repository: AccountRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputUpdateAccountPasswordDto) -> None:
        user = self.repository.find(input_dto.get('id'))

        # check username
        if user.username != input_dto.get('username'):
            raise UserNotFound

        # check password
        if not user.verify_password(input_dto.get('password')):
            raise UserNotFound

        # check new password policies
        # hash new password
        user.generate_hashed_password(input_dto.get('new_password'))

        # update password
        self.repository.update(user)
        return
