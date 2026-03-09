from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, db):
        self.db = db
        self.repo = UserRepository(db)

    def get_user(self, user_id: int):
        try:
            with self.db.begin():
                return self.repo.get_by_id(user_id)
        except:
            self.db.rollback()
            raise

    def get_all_users(self):
        try:
            with self.db.begin():
                return self.repo.list_users()
        except:
            self.db.rollback()
            raise
