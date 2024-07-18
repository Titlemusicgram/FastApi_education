from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Таблица очищена')
    await create_tables()
    print('Таблица готова к работе')
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
