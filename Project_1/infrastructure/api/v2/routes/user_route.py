import os
from typing import Optional
from fastapi import status, HTTPException, APIRouter, Depends
from dotenv import load_dotenv

from domain.auth.entity.auth import Auth
from domain.user.exceptions.user_exceptions import UserNotFound
from infrastructure.user.repository.dict.user_repository import UserRepositoryDict
from infrastructure.user.repository.postgres.user_repository import UserRepositoryPostgres
from infrastructure.user.repository.sqlite.user_repository import UserRepositorySqlite
from usecase.auth.get.get_user_dto import OutputGetUserDto
from usecase.user.find.find_user_dto import InputFindUserDto, OutputFindUserDto
from usecase.user.find.find_user_usecase import FindUserUseCase
from usecase.user.find_all.find_all_user_dto import OutputFindAllUserDto
from usecase.user.find_all.find_all_user_usecase import FindAllUserUseCase

load_dotenv()
REPOSITORY = os.environ.get("REPOSITORY")
if REPOSITORY == 'sqlite':
    user_repository = UserRepositorySqlite()
elif REPOSITORY == 'postgresql':
    user_repository = UserRepositoryPostgres()
elif REPOSITORY == 'dict':
    user_repository = UserRepositoryDict()

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
    except Exception:
        raise HTTPException(status_code=500,
                            detail="Something went wrong :(")


@router.get("/{user_id}")
async def find_user(user_id: str,
                    user_auth: OutputGetUserDto = Depends(Auth.get_current_user)):
    try:
        input_dto: InputFindUserDto = {"id": user_id}
        output_dto: OutputFindUserDto = FindUserUseCase(user_repository).execute(input_dto)
        return output_dto
    except UserNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not found')
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Something went wrong :(")
