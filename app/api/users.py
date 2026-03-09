from typing import Annotated
from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User

router = APIRouter()

@router.get("/users/me")
def get_user(user_id: int, db: Annotated[Session, Depends(get_db) ]):
    return UserService(db).get_user(user_id)

@router.get("/users")
def get_users(current_user: Annotated[User, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)]):
    AuthService(db).authorize_admin(current_user)
    return UserService(db).get_all_users()
