import sys

from starlette.responses import RedirectResponse

sys.path.append("..")

from sqlalchemy.orm import Session
from fastapi import Depends, status, APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import models
# from infrastructure.sqlite.database import engine, SessionLocal
from infrastructure.postgres.database import engine, SessionLocal
# from infrastructure.mysql.database import engine, SessionLocal
from .auth import get_current_user, get_password_hash, verify_password

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"description": "Not found"}})

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/update-password", response_class=HTMLResponse)
async def update_password(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse("/auth", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("update-password.html", {"request": request, "user": user})


@router.post("/update-password")
async def update_password(request: Request,
                          username: str = Form(...),
                          password: str = Form(...),
                          new_password: str = Form(...),
                          db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse("/auth", status_code=status.HTTP_302_FOUND)

    user_model = db.query(models.Users)\
        .filter(models.Users.id == user.get("id"))\
        .first()

    if user_model is None:
        return RedirectResponse("/auth", status_code=status.HTTP_302_FOUND)

    if username != user_model.username \
            or not verify_password(password, user_model.hashed_password):
        msg = "Verify username and password fields"
        return templates.TemplateResponse("update-password.html", {"request": request, "msg": msg, "msg_type": "error", "user": user})

    if len(new_password) <= 3:
        msg = "New Password must have more than 3 characters"
        return templates.TemplateResponse("update-password.html", {"request": request, "msg": msg, "msg_type": "error", "user": user})

    hash_password = get_password_hash(new_password)
    user_model.hashed_password = hash_password

    db.add(user_model)
    db.commit()

    msg = "Password successfully updated"
    return templates.TemplateResponse("update-password.html", {"request": request, "msg": msg, "msg_type": "success", "user": user})

