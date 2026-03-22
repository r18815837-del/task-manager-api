from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "todo"


class TaskCreate(TaskBase):
    project_id: int
    assignee_id: int | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    assignee_id: int | None = None


class TaskRead(TaskBase):
    id: int
    project_id: int
    creator_id: int
    assignee_id: int | None = None

    model_config = ConfigDict(from_attributes=True)