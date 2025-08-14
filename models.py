from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlmodel.main import uuid
from datetime import datetime


class Task(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True, index=True
    )
    title: str
    content: str
    owned_by: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.now)
    due_at: datetime


postgres_url = (
    "postgresql://todolist-admin:password@database:5432/todolist-app"
)

engine = create_engine(postgres_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
