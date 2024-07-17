from fastapi import FastAPI
from routers import tasks_router
from contextlib import asynccontextmanager
from models import delete_tables, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Таблица очищена')
    await create_tables()
    print('Таблица создана')
    yield
    print('Выключение БД')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
