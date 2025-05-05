from sqlalchemy import Column, Integer, String
from database import Base
from datetime import datetime
from zoneinfo import ZoneInfo

# definimos o fuso horário BR-SP
TZ = ZoneInfo("America/Sao_Paulo")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    create_date = Column(
        String(45),
        default=lambda: datetime.now(TZ).isoformat()
    )
    update_date = Column(
        String(45),
        default=lambda: datetime.now(TZ).isoformat(),
        onupdate=lambda: datetime.now(TZ).isoformat()
    )

class BookDelete(Base):
    __tablename__ = "books_delete"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    delete_date = Column(
        String(45),
        default=lambda: datetime.now(TZ).isoformat()
    )
