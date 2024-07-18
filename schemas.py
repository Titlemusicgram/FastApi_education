from pydantic import BaseModel, ConfigDict


class ScmTaskAdd(BaseModel):
    name: str
    description: str | None = None


class ScmTask(ScmTaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ScmTaskId(BaseModel):
    ok: bool = True
    task_id: int
