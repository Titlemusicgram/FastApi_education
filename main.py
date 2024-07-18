from fastapi import FastAPI
from database import create_tables, delete_tables
from router import tasks_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Таблица очищена')
    await create_tables()
    print('Таблица готова к работе')
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
