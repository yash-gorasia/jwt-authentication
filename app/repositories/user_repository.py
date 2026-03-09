from app.models.user import User
from sqlalchemy.orm import Session

class UserRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_user(self):
        ...
