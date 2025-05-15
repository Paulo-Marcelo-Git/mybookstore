# mybookstore\bookstore-api\models.py

from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class TimestampMixin:
    create_date = Column(
        DateTime(timezone=True),
        default=func.now(),
        nullable=False
    )
    update_date = Column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

class Book(Base, TimestampMixin):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}')>"

class BookDelete(Base):
    __tablename__ = "books_delete"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    delete_date = Column(
        DateTime(timezone=True),
        default=func.now(),
        nullable=False
    )

    def __repr__(self):
        return f"<BookDelete(id={self.id}, title='{self.title}')>"
