from datetime import datetime, timedelta, timezone
import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

from sqlalchemy.orm import Session

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def authorize_admin(self):
        with self.db.begin():
            ...
