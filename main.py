from fastapi import FastAPI
from tasks_router import tasks_router
from database import create_table, delete_table
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_table()
    # await create_table()
    print('Сервер запущен!')
    yield


app = FastAPI(title="Tasks_service", lifespan=lifespan)
app.include_router(tasks_router)
