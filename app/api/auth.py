from fastapi import APIRouter

router = APIRouter()

@router.post("/auth/register")
def register_user():
    return {"message": "register user"}

@router.post("/auth/login")
def login_user():
    return {"message": "login user"}

@router.post("/auth/refresh")
def refresh_token():
    return {"message": "refresh token"}
