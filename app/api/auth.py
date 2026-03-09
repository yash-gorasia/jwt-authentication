from typing import Annotated

from fastapi import APIRouter, Depends
from app.db.session import get_db
from sqlalchemy.orm import Session

from app.services.auth_service import AuthService
from app.schemas.user import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse




router = APIRouter()

@router.post("/auth/register", response_model=RegisterResponse)
def register_user(payload: RegisterRequest, db: Annotated[Session, Depends(get_db)]):
    return AuthService(db).register(payload)

@router.post("/auth/login", response_model=LoginResponse)
def login_user(payload: LoginRequest, db: Annotated[Session, Depends(get_db)]):
    return AuthService(db).login(payload)

@router.post("/auth/refresh")
def refresh_token():
    return {"message": "refresh token"}
