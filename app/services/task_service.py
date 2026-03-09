from app.repositories.task_repository import TaskRepository
from sqlalchemy.orm import Session

class TaskService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = TaskRepository(db)

    def create_task(self, payload):
        try:
            with self.db.begin():
                return self.repo.create_task_db(payload.model_dump())
        except:
            self.db.rollback()
            raise

    def get_task_current_user_id(self, user_id):
        try:
            with self.db.begin():
                return self.repo.get_user_tasks_db(user_id)
        except:
            self.db.rollback()
            raise

    def get_task_by_id(self, task_id: int):
        try:
            with self.db.begin():
                return self.repo.get_by_id_db(task_id)
        except:
            self.db.rollback()
            raise

    def update_task(self, task_id, payload):
        try:
            with self.db.begin():
               data = payload.dict(exclude_unset=True)
               return self.repo.update_task_db(task_id, **data)
        except:
            self.db.rollback()
            raise

    def delete_task(self, task_id):
        try:
            with self.db.begin():
                return self.repo.delete_task_db(task_id)
        except:
            self.db.rollback()
            raise
