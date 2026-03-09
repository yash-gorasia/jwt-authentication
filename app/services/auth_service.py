from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository

from app.core.security import  hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepository(db)

    def authorize_admin(self, user):
            if user.role != "admin":
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Admin only route.")

    def register(self, payload):
        try:
                hashed = hash_password(payload.password)
                payload.password = hashed

                with self.db.begin():
                    return self.repo.create_user_db(payload.model_dump())

        except:
            self.db.rollback()
            raise

    def login(self, payload):
        try:
            with self.db.begin():
                user = self.repo.get_by_email(payload.email)

                if not user:
                    return None
                if not verify_password(payload.password, user.password):
                    return None

                token = create_access_token(
                    {"user_id": user.user_id, "role": user.role}
                )

                return token
        except:
            self.db.rollback()
            raise
