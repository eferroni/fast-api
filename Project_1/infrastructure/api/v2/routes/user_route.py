from typing import Optional
from fastapi import status, HTTPException, APIRouter, Depends

from domain.auth.entity.auth import Auth
from usecase.auth.get.get_user_dto import OutputGetUserDto
from usecase.user.find.find_user_dto import InputFindUserDto, OutputFindUserDto
from usecase.user.find.find_user_usecase import FindUserUseCase
from usecase.user.find_all.find_all_user_dto import OutputFindAllUserDto
from usecase.user.find_all.find_all_user_usecase import FindAllUserUseCase
from infrastructure.user.repository.repository import user_repository


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def find_all_users(user_id: Optional[str] = None,
                         user_auth: OutputGetUserDto = Depends(Auth.get_current_user)):
    try:
        input_dto = {}
        if user_id is not None:
            input_dto['id'] = user_id
        use_case = FindAllUserUseCase(user_repository)
        output_dto: list[OutputFindAllUserDto] = use_case.execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.get("/{user_id}")
async def find_user(user_id: str,
                    user_auth: OutputGetUserDto = Depends(Auth.get_current_user)):
    try:
        input_dto: InputFindUserDto = {"id": user_id}
        output_dto: OutputFindUserDto = FindUserUseCase(user_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")
