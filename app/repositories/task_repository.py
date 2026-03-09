from app.models.task import Task
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_task_db(self, data: dict) -> Task:
        new_task = Task(**data)
        self.db.add(new_task)
        self.db.flush()

        return new_task

    def get_user_tasks_db(self, user_id: int):
        return self.db.execute(select(Task).where(Task.user_id == user_id)).all()

    def get_by_id_db(self, task_id: int):
        return self.db.execute(select(Task).where(Task.task_id == task_id)).all()

    def update_task_db(self, task_id: int, **data: dict) -> Task:
        task = self.db.get(Task, task_id)

        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found.")

        for key, value in data.items():
            setattr(task, key, value)

        self.db.flush()

        return task

    def delete_task_db(self, task_id: int):
        return self.db.execute(delete(Task).where(Task.task_id == task_id))
