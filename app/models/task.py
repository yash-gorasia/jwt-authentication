from sqlalchemy import Integer, Text, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schemas.task import TaskStatus

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.PENDING)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_id"))

    user = relationship("User", back_populates="tasks")
