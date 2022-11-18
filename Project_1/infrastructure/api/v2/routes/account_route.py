from fastapi import status, HTTPException, APIRouter, Depends

from domain.auth.entity.auth import get_current_user
from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from infrastructure.api.v2.validator.account.update_account_validator import UpdateAccountValidator
from infrastructure.api.v2.validator.account.update_account_password_validator import UpdateAccountPasswordValidator
from usecase.account.activate.activate_account_dto import InputActivateAccountDto
from usecase.account.activate.activate_account_usecase import ActivateAccountUseCase
from usecase.account.deactivate.deactivate_account_dto import InputDeactivateAccountDto
from usecase.account.deactivate.deactivate_account_usecase import DeactivateAccountUseCase
from usecase.account.delete.delete_account_dto import InputDeleteAccountDto
from usecase.account.delete.delete_account_usecase import DeleteAccountUseCase
from usecase.account.update_account.update_account_dto import InputUpdateAccountDto, OutputUpdateAccountDto
from usecase.account.update_account.update_account_usecase import UpdateAccountUseCase
from usecase.account.update_password.update_account_password_dto import InputUpdateAccountPasswordDto
from usecase.account.update_password.update_account_password_usecase import UpdateAccountPasswordUseCase
from usecase.auth.get.get_user_dto import OutputGetUserDto
from infrastructure.account.repository.repository import account_repository

router = APIRouter(prefix="/account", tags=["account"])


@router.put("/{user_id}")
async def update_user_account(user_id: str,
                              user: UpdateAccountValidator,
                              user_auth: OutputGetUserDto = Depends(get_current_user)):
    try:
        if user_id != user_auth.get('id'):
            raise AuthUnauthorizedException
        input_dto: InputUpdateAccountDto = {"id": user_auth.get('id'),
                                            "email": user.email,
                                            "first_name": user.first_name,
                                            "last_name": user.last_name}
        output_dto: OutputUpdateAccountDto = UpdateAccountUseCase(account_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.put("/{user_id}/password", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_account_password(user_id: str,
                                       user: UpdateAccountPasswordValidator,
                                       user_auth: OutputGetUserDto = Depends(get_current_user)):
    try:
        if user_id != user_auth.get('id'):
            raise AuthUnauthorizedException
        input_dto: InputUpdateAccountPasswordDto = {
            "id": user_auth.get('id'),
            "username": user.username,
            "password": user.password,
            "new_password": user.new_password
        }
        UpdateAccountPasswordUseCase(account_repository).execute(input_dto)
        return
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.put("/{user_id}/activate", status_code=status.HTTP_204_NO_CONTENT)
async def activate_user_account(user_id: str,
                                user_auth: OutputGetUserDto = Depends(get_current_user)):
    try:
        if user_id != user_auth.get('id'):
            raise AuthUnauthorizedException
        input_dto: InputActivateAccountDto = {"id": user_auth.get('id')}
        ActivateAccountUseCase(account_repository).execute(input_dto)
        return
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.put("/{user_id}/deactivate", status_code=status.HTTP_204_NO_CONTENT)
async def deactivate_user_account(user_id: str,
                                  user_auth: OutputGetUserDto = Depends(get_current_user)):
    try:
        if user_id != user_auth.get('id'):
            raise AuthUnauthorizedException
        input_dto: InputDeactivateAccountDto = {"id": user_auth.get('id')}
        DeactivateAccountUseCase(account_repository).execute(input_dto)
        return
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_account(user_id: str,
                              user_auth: OutputGetUserDto = Depends(get_current_user)):
    try:
        if user_id != user_auth.get('id'):
            raise AuthUnauthorizedException
        input_dto: InputDeleteAccountDto = {"id": user_auth.get('id')}
        DeleteAccountUseCase(account_repository).execute(input_dto)
        return
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")
