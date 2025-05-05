import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from main import app, get_db
import models

# Banco de dados SQLite em memória
SQLALCHEMY_TEST_DB_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Substitui a dependência do banco por uma sessão com SQLite e cria as tabelas
def override_get_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Aplicando a substituição no app
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={
        "title": "Livro de Teste",
        "author": "Autor Teste",
        "description": "Descrição fictícia"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Livro de Teste"
    assert data["author"] == "Autor Teste"
    assert "id" in data
    assert "create_date" in data

def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
