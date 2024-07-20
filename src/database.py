from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import settings
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.get_url_db)
session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
