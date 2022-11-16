from pydantic import BaseModel, Field


class UpdateAccountValidator(BaseModel):
    email: str = Field(min_length=1, max_length=100)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "email": "john@email.com",
                "first_name": "John",
                "last_name": "Doe",
            }
        }
