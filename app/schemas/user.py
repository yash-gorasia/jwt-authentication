from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    email: EmailStr
    password: str
class RegisterRequest(UserBase):
    name: str

class RegisterResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

class LoginRequest(UserBase):
    ...

class LoginResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
