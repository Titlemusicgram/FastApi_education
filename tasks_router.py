from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STaskAdd, STaskId, STask, STaskDelete, STaskEdit

tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])


@tasks_router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks


@tasks_router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> list[STaskId]:
    task_id = await TaskRepository.add_one(task)
    return task_id


@tasks_router.delete("")
async def delete_task(task: Annotated[STaskId, Depends()]) -> list[STaskDelete]:
    deleted_id = await TaskRepository.delete_task(task)
    return deleted_id


@tasks_router.post("/edit")
async def edit_task(task_edit: Annotated[STaskEdit, Depends()]) -> list[STask]:
    task = await TaskRepository.edit_task(task_edit)
    return task
