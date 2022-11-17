from fastapi import status, HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from infrastructure.api.v2.validator.auth.create_user_validator import CreateUserValidator
from usecase.auth.create.create_user_dto import InputCreateUserDto, OutputCreateUserDto
from usecase.auth.create.create_user_usecase import CreateUserUseCase
from usecase.auth.login.login_user_dto import InputLoginUserDto, OutputLoginUserDto
from usecase.auth.login.login_user_usecase import LoginUserUseCase
from infrastructure.auth.repository.repository import auth_repository


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
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        input_dto: InputLoginUserDto = {"username": form_data.username,
                                        "password": form_data.password}
        output_dto: OutputLoginUserDto = LoginUserUseCase(auth_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")
