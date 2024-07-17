from pydantic import BaseModel


class AddTask(BaseModel):
    name: str
    description: str | None = None


class Task(AddTask):
    id: int
