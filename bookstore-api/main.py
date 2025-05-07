from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.responses import HTMLResponse, FileResponse
from sqlalchemy.orm import Session
from datetime import datetime
from zoneinfo import ZoneInfo
import logging
import time
import models, schemas
from database import SessionLocal, engine

# 🔧 Logging genérico
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

TZ = ZoneInfo("America/Sao_Paulo")

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bookstore API",
    openapi_tags=[
        {"name": "Listagem", "description": "Rotas de listagem"},
        {"name": "CRUD", "description": "Criação, leitura, atualização e remoção"},
        {"name": "Docs", "description": "Documentação estática"},
    ]
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = f"{request.method} {request.url.path}"
    logger.info(f"→ {idem}")
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"← {idem} - {response.status_code} ({duration:.2f}s)")
    return response

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books/", response_model=list[schemas.BookSummary], tags=["Listagem"])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.post("/books/", response_model=schemas.Book, tags=["CRUD"], status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/{book_id}", response_model=schemas.Book, tags=["CRUD"])
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.Book, tags=["CRUD"])
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    for key, value in book.model_dump().items():
        setattr(db_book, key, value)
    db_book.update_date = datetime.now(TZ)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["CRUD"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    db_del = models.BookDelete(
        title=db_book.title,
        author=db_book.author,
        description=db_book.description,
        delete_date=datetime.now(TZ)
    )
    db.add(db_del)
    db.delete(db_book)
    db.commit()
    return None

@app.get("/documentation", response_class=HTMLResponse, tags=["Docs"])
def get_documentation():
    return FileResponse("docs/index.html")

@app.get("/", tags=["Docs"])
def root():
    return {"message": "API está no ar!"}
