from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

url = "sqlite+aiosqlite:///tasks_base.db"

engine = create_async_engine(url)
session_factory = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
