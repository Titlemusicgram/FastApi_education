from sqlalchemy.orm import mapped_column, Mapped
from src.database import Base


class TTask(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
