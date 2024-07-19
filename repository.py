from sqlalchemy import select, delete, update
from database import session_factory
from models import TTask
from schemas import STaskAdd, STask, STaskId, STaskDelete, STaskEdit


class TaskRepository:
    @classmethod
    async def get_all(cls) -> list[STask]:
        async with session_factory() as session:
            query = select(TTask)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks

    @classmethod
    async def add_one(cls, s_task: STaskAdd) -> list[STaskId]:
        async with session_factory() as session:
            task_dict = s_task.model_dump()
            task = TTask(**task_dict)
            session.add(task)
            await session.flush()
            json_resp = [{'id': task.id}]
            await session.commit()
            return json_resp

    @classmethod
    async def delete_task(cls, s_task: STaskId) -> list[STaskDelete]:
        async with session_factory() as session:
            query = delete(TTask).where(TTask.id == s_task.id)
            await session.execute(query)
            await session.commit()
            json_resp = [{"id": s_task.id, "status": "deleted"}]
            return json_resp

    @classmethod
    async def edit_task(cls, s_task: STaskEdit) -> list[STask]:
        async with (session_factory() as session):
            task_dict = s_task.model_dump()
            task_dict = {k: v for k, v in task_dict.items() if k != 'id' and v is not None}
            query = update(TTask).where(TTask.id == s_task.id).values(task_dict).returning(TTask)
            result = await session.execute(query)
            task = result.scalars().one()
            await session.flush()
            await session.commit()
            task = [STask.model_validate(task)]
            return task
