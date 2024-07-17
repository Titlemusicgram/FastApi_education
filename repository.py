from sqlalchemy import select
from database import session_factory
from models import TaskTable
from schemas import AddTask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: AddTask) -> int:
        async with session_factory() as session:
            task_dict = data.model_dump()
            task = TaskTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        async with session_factory() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
