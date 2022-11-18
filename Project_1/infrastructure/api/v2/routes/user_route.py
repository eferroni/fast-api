from typing import Optional, Literal
from fastapi import status, HTTPException, APIRouter, Depends

from domain.auth.entity.auth import get_current_active_user
from infrastructure.api.v2.__shared__.parameters import OutputCommonParametersDto, common_parameters
from usecase.auth.get.get_user_dto import OutputGetUserDto
from usecase.user.find.find_user_dto import InputFindUserDto, OutputFindUserDto
from usecase.user.find.find_user_usecase import FindUserUseCase
from usecase.user.find_all.find_all_user_dto import OutputFindAllUserDto, InputFindAllUserDto
from usecase.user.find_all.find_all_user_usecase import FindAllUserUseCase
from infrastructure.user.repository.repository import user_repository


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def find_all_users(username: Optional[str] = None,
                         email: Optional[str] = None,
                         first_name: Optional[str] = None,
                         last_name: Optional[str] = None,
                         order: Literal['username', 'email', 'first_name', 'last_name'] = 'username',
                         user_auth: OutputGetUserDto = Depends(get_current_active_user),
                         commons: OutputCommonParametersDto = Depends(common_parameters)):
    try:
        input_dto: InputFindAllUserDto = {
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'page': commons.get('page'),
            'size': commons.get('size'),
            'order': order
        }
        use_case = FindAllUserUseCase(user_repository)
        output_dto: OutputFindAllUserDto = use_case.execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.get("/{user_id}")
async def find_user(user_id: str,
                    user_auth: OutputGetUserDto = Depends(get_current_active_user)):
    try:
        input_dto: InputFindUserDto = {"id": user_id}
        output_dto: OutputFindUserDto = FindUserUseCase(user_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")
