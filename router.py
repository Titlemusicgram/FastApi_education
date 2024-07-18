from typing import List, Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import SAddTask, STask, STaskId

tasks_router = APIRouter(prefix='/tasks', tags=['Tasks'])


@tasks_router.get('')
async def get_tasks() -> List[STask]:
    task_models = await TaskRepository.find_all()
    tasks = [STask.validate(task_model) for task_model in task_models]
    return tasks


@tasks_router.post('')
async def add_task(task: Annotated[SAddTask, Depends()]) -> list[STaskId]:
    task_id = await TaskRepository.add_one(task)
    return [{'ok': True, 'task_id': task_id}]
