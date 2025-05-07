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

    class Config:
        from_attributes = True


# Nova schema para retorno enxuto
class BookSummary(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True
