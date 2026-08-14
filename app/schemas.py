from pydantic import BaseModel
from pydantic import ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TaskOut(TaskBase):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)