from pydantic import BaseModel, Field


class CreateUserValidator(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=1, max_length=100)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "username": "john",
                "email": "john@email.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "Test1234!"
            }
        }
