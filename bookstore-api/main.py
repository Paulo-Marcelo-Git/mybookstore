from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse, FileResponse
from sqlalchemy.orm import Session
from datetime import datetime
from zoneinfo import ZoneInfo
import models, schemas
from database import SessionLocal, engine

# mesmo fuso usado nos models
TZ = ZoneInfo("America/Sao_Paulo")

# cria as tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bookstore API",
    openapi_tags=[
        {"name": "Listagem", "description": "Rotas de listagem"},
        {"name": "CRUD",      "description": "Criação, leitura, atualização e remoção"},
        {"name": "Docs",      "description": "Documentação estática"},
    ]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota de listagem enxuta — só IDs e titles
@app.get("/books/", response_model=list[schemas.BookSummary], tags=["Listagem"])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# Criação de livro
@app.post("/books/", response_model=schemas.Book, tags=["CRUD"])
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Leitura de um livro
@app.get("/books/{book_id}", response_model=schemas.Book, tags=["CRUD"])
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Atualização de um livro
@app.put("/books/{book_id}", response_model=schemas.Book, tags=["CRUD"])
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db_book.update_date = datetime.now(TZ).isoformat()
    db.commit()
    db.refresh(db_book)
    return db_book

# Remoção de um livro
@app.delete("/books/{book_id}", tags=["CRUD"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_del = models.BookDelete(
        title=db_book.title,
        author=db_book.author,
        description=db_book.description,
        delete_date=datetime.now(TZ).isoformat()
    )
    db.add(db_del)
    db.delete(db_book)
    db.commit()
    return {"ok": True}

# Documentação estática
@app.get("/documentation", response_class=HTMLResponse, tags=["Docs"])
def get_documentation():
    return FileResponse("docs/index.html")
