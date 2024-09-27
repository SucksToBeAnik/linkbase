import uuid
from sqlmodel import Field, SQLModel
from uuid import UUID


class Link(SQLModel, table=True):
    __tablename__ = 'links'
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, unique=True)
    title: str