from pydantic import BaseModel, ConfigDict, Field


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    id: int


class STaskDelete(BaseModel):
    id: int
    status: str


class STaskEdit(STaskId):
    name: str | None = Field(alias='new_name', default=None)
    description: str | None = Field(alias='new_description', default=None)
