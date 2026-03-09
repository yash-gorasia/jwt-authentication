from fastapi import APIRouter

router =  APIRouter()

@router.post("/tasks")
def create_task():
    return {"message": "create task"}

@router.get("/tasks")
def current_user_task():
    return {"message": "list current users's tasks"}

@router.get("/tasks/{id}")
def get_task():
    return {"message": "get specific task"}

@router.put("/tasks/{id}")
def update_task():
    return {"message": "update task"}

@router.delete("/tasks/{id}")
def delete_task():
    return {"message": "delete task"}
