from app.models.user import User
from sqlalchemy import select
from sqlalchemy.orm import Session

class UserRepository():
    def __init__(self, db: Session):
        self.db = db

    def create_user_db(self, data: dict) -> User:
        new_user = User(**data)
        self.db.add(new_user)
        self.db.flush()

        return new_user

    def get_by_email(self, email: str):
        return self.db.execute(select(User).where(User.email == email)).fetchone()

    def get_by_id(self, user_id: int):
        return self.db.execute(select(User).where(User.user_id == user_id)).fetchone()

    def list_users(self):
        return self.db.execute(select(User)).all()
