from pydantic import BaseModel, ConfigDict


class SAddTask(BaseModel):
    name: str
    description: str | None = None


class STask(SAddTask):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
