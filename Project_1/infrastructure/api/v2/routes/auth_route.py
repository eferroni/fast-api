import os
from dotenv import load_dotenv
from fastapi import status, HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from domain.auth.exceptions.auth_exceptions import AuthUnauthorizedException
from domain.user.exceptions.user_exceptions import UserAlreadyExist, PasswordPolicy
from infrastructure.api.v2.validator.auth.create_user_validator import CreateUserValidator
from infrastructure.auth.repository.dict.auth_repository import AuthRepositoryDict
from infrastructure.auth.repository.postgres.auth_repository import AuthRepositoryPostgres
from infrastructure.auth.repository.sqlite.auth_repository import AuthRepositorySqlite
from usecase.auth.create.create_user_dto import InputCreateUserDto, OutputCreateUserDto
from usecase.auth.create.create_user_usecase import CreateUserUseCase
from usecase.auth.login.login_user_dto import InputLoginUserDto, OutputLoginUserDto
from usecase.auth.login.login_user_usecase import LoginUserUseCase

load_dotenv()
REPOSITORY = os.environ.get("REPOSITORY")
if REPOSITORY == 'sqlite':
    auth_repository = AuthRepositorySqlite()
elif REPOSITORY == 'postgresql':
    auth_repository = AuthRepositoryPostgres()
elif REPOSITORY == 'dict':
    auth_repository = AuthRepositoryDict()

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserValidator):
    try:
        input_dto: InputCreateUserDto = {"username": user.username,
                                         "email": user.email,
                                         "first_name": user.first_name,
                                         "last_name": user.last_name,
                                         "password": user.password}
        output_dto: OutputCreateUserDto = CreateUserUseCase(auth_repository).execute(input_dto)
        return output_dto

    except UserAlreadyExist as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=str(e))
    except PasswordPolicy as f:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(f))
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Something went wrong :(")


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        input_dto: InputLoginUserDto = {"username": form_data.username,
                                        "password": form_data.password}
        output_dto: OutputLoginUserDto = LoginUserUseCase(auth_repository).execute(input_dto)
        return output_dto

    except AuthUnauthorizedException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or password')
    # except Exception:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                         detail="Something went wrong :(")

