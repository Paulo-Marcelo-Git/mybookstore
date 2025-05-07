from pydantic import BaseModel
from datetime import datetime


class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    create_date: datetime
    update_date: datetime

    model_config = {
        "from_attributes": True
    }


class BookSummary(BaseModel):
    id: int
    title: str

    model_config = {
        "from_attributes": True
    }
