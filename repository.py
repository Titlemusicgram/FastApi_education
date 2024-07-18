from database import new_session, TTasks
from schemas import ScmTaskAdd, ScmTask, ScmTaskId
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: ScmTaskAdd) -> ScmTaskId:
        async with new_session() as session:
            task_dist = data.model_dump()
            task = TTasks(**task_dist)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[ScmTask]:
        async with new_session() as session:
            query = select(TTasks)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [ScmTask.model_validate(task_model) for task_model in task_models]
            return task_schemas
