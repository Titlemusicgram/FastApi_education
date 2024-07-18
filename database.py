from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from models import Base
from config import settings


url = settings.db_url_asyncpg
engine = create_async_engine(url)
session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
