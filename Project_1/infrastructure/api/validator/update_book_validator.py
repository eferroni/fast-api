from pydantic import BaseModel, Field


class UpdateBookValidator(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "title": "Computer Science Pro",
                "author": "Eduardo",
            }
        }
