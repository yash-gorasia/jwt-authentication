from typing import Annotated
from fastapi import APIRouter, Depends
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.models.user import User

from app.schemas.task import TaskRequest, TaskResponse, TaskUpdateRequest
from app.services.task_service import TaskService

router =  APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(payload: TaskRequest, db: Annotated[Session, Depends(get_db)] ):
    return TaskService(db).create_task(payload)

@router.get("/tasks")
def current_user_task(current_user: Annotated[User, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)]):
    return TaskService(db).get_task_current_user_id(current_user.user_id)

@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    return TaskService(db).get_task_by_id(task_id)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, payload: TaskUpdateRequest, db: Annotated[Session, Depends(get_db)]):
    return TaskService(db).update_task(task_id, payload)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    return TaskService(db).delete_task(task_id)
