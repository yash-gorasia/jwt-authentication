from typing import Annotated

from fastapi import APIRouter, Depends
from app.schemas.user import RegisterUserRequest, RegisterUserResponse
from app.db.session import get_db

from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/auth/register", response_model=RegisterUserResponse)
def register_user(payload: RegisterUserRequest, db: Annotated[Session, Depends(get_db)]):
    return 


@router.post("/auth/login")
def login_user():
    return {"message": "login user"}


@router.post("/auth/refresh")
def refresh_token():
    return {"message": "refresh token"}
