from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database import create_tables, delete_tables
from src.tasks.tasks_router import tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # await create_tables()
    yield


app = FastAPI(title='Tasks', lifespan=lifespan)
app.include_router(tasks_router)
