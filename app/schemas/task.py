import enum
from pydantic import BaseModel, ConfigDict

class TaskStatus(enum.Enum):
    COMPLETED =  "completed"
    PENDING = "pending"

class TaskRequest(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str
    status: str
