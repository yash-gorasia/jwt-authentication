from pydantic import BaseModel
from app.schemas.user import User

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
