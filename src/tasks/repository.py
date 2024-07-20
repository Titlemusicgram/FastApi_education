from src.tasks.schemas import STask, STaskId, STaskEdit, STaskAdd, STaskDeleted
from src.database import session_factory
from src.tasks.models import TTask
from sqlalchemy import select, delete, update


class TaskRepository:
    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with session_factory() as session:
            query = select(TTask)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks

    @classmethod
    async def add_task(cls, s_task: STaskAdd) -> list[STaskId]:
        async with session_factory() as session:
            task_dict = s_task.model_dump()
            task = TTask(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            json_resp = [{"id": task.id}]
            return json_resp

    @classmethod
    async def delete_task(cls, task_id: STaskId) -> list[STaskDeleted]:
        async with session_factory() as session:
            query = delete(TTask).where(TTask.id == task_id.id).returning(TTask)
            result = await session.execute(query)
            deleted_task = result.scalars().one_or_none()
            deleted_id = [{"id": deleted_task.id,
                           "status": "deleted"}] if deleted_task else [{"id": task_id.id,
                                                                        "status": "id is not existing"}]
            await session.commit()
            return deleted_id

    @classmethod
    async def edit_task(cls, s_task: STaskEdit) -> list[STask]:
        async with session_factory() as session:
            task_dict = s_task.model_dump()
            task_dict = {k: v for k, v in task_dict.items() if k != 'id' and v is not None}
            query = update(TTask).where(TTask.id == s_task.id).values(**task_dict).returning(TTask)
            result = await session.execute(query)
            edited_task = result.scalars().one_or_none()
            await session.commit()
            if_not_exist = [{
                "id": s_task.id,
                "name": "id is not exist",
                # "description": "id is not exist"
            }]
            s_edited_task = [STask.model_validate(edited_task)] if edited_task else if_not_exist
            return s_edited_task
