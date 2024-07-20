from pydantic import BaseModel, ConfigDict, Field


class STaskAdd(BaseModel):
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    id: int


class STaskDeleted(BaseModel):
    id: int
    status: str


class STaskEdit(STask):
    id: int
    name: str | None = Field(alias="new_name", default=None)
    description: str | None = Field(alias="new_description", default=None)
