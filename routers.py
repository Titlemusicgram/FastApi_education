from typing import List, Annotated
from fastapi import APIRouter, Depends
from schemas import Task, AddTask
from repository import TaskRepository

tasks_router = APIRouter(prefix='/tasks', tags=['Tasks'])


@tasks_router.get('')
async def get_tasks() -> List[Task]:
    tasks = await TaskRepository.find_all()
    return tasks


@tasks_router.post('')
async def add_task(task: Annotated[AddTask, Depends()]):
    task_id = await TaskRepository.add_one(task)
    return [task_id]
