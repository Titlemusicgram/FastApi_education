from database import session_factory
from models import TTask
from schemas import SAddTask
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, s_task: SAddTask) -> int:
        async with session_factory() as session:
            task_dict = s_task.model_dump()
            task = TTask(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[TTask]:
        async with session_factory() as session:
            query = select(TTask)
            result = await session.execute(query)
            tasks = result.scalars().all()
            return tasks
