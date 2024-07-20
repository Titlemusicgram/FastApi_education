from typing import Annotated
from fastapi import APIRouter, Depends
from src.tasks.repository import TaskRepository
from src.tasks.schemas import STask, STaskId, STaskEdit, STaskAdd, STaskDeleted

tasks_router = APIRouter(tags=['Tasks'], prefix='/tasks')


@tasks_router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks


@tasks_router.post('')
async def add_task(task: Annotated[STaskAdd, Depends()]) -> list[STaskId]:
    task_id = await TaskRepository.add_task(task)
    return task_id


@tasks_router.delete('')
async def delete_task(task_id: Annotated[STaskId, Depends()]) -> list[STaskDeleted]:
    deleted_task = await TaskRepository.delete_task(task_id)
    return deleted_task


@tasks_router.post('/edit_task')
async def edit_task(task: Annotated[STaskEdit, Depends()]) -> list[STask]:
    edited_task = await TaskRepository.edit_task(task)
    return edited_task
