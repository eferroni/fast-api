from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def get_company_name():
    return {"company_name": "Example Company, LLC"}


@router.get("/employees")
def number_of_employees():
    return 162