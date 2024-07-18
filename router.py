from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import ScmTaskAdd, ScmTask, ScmTaskId

router = APIRouter(prefix='/tasks', tags=['Таски'])


@router.post('')
async def add_task(task: Annotated[ScmTaskAdd, Depends()]) -> ScmTaskId:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_tasks() -> list[ScmTask]:
    tasks = await TaskRepository.find_all()
    return tasks
