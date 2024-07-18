from models import TTask
from schemas import STaskAdd, STask
from database import session_factory
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_task(cls, s_task: STaskAdd) -> int:
        async with session_factory() as session:
            task_dict = s_task.model_dump()
            task = TTask(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with session_factory() as session:
            query = select(TTask)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.validate(task_model) for task_model in task_models]
            return tasks
