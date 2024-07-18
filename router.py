from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import STaskAdd, STaskId, STask
from repository import TaskRepository

task_router = APIRouter(prefix='/tasks', tags=['Tasks'])


@task_router.post('')
async def add_task(task: Annotated[STaskAdd, Depends()]) -> list[STaskId]:
    task_id = await TaskRepository.add_task(task)
    return [{'task_id': task_id}]


@task_router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks
