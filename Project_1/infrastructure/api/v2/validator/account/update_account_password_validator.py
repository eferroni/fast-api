from pydantic import BaseModel, Field


class UpdateAccountPasswordValidator(BaseModel):
    username: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=100)
    new_password: str = Field(min_length=1, max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "username": "john",
                "password": "Test1234!",
                "new_password": "Test5678!",
            }
        }
