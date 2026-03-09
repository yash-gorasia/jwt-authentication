from fastapi import APIRouter

router = APIRouter()

@router.get("/users/me")
def get_current_user():
    return {"message": "current user"}

@router.get("/users")
def get_users():
    return {"message": "List of users"}
