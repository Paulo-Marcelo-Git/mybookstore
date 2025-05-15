# \bookstore-api\tests\test_books.py

import pytest
from fastapi import status

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "API está no ar!"}

def test_create_book(client):
    payload = {"title": "Clean Code", "author": "Robert C. Martin", "description": "Código limpo."}
    response = client.post("/books/", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert "id" in data
    assert "create_date" in data
    assert "update_date" in data

def test_create_book_invalid(client):
    # Falta o campo title
    response = client.post("/books/", json={"author": "A", "description": ""})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_list_books(client):
    client.post("/books/", json={"title": "Livro 1", "author": "Autor 1", "description": ""})
    response = client.get("/books/")
    assert response.status_code == status.HTTP_200_OK
    livros = response.json()
    assert isinstance(livros, list)
    assert any(book["title"] == "Livro 1" for book in livros)

def test_read_book_not_found(client):
    response = client.get("/books/999999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Livro não encontrado"

def test_update_book(client):
    new_book = client.post("/books/", json={"title": "Old", "author": "A", "description": "desc"}).json()
    response = client.put(f"/books/{new_book['id']}", json={"title": "New", "author": "B", "description": "Updated"})
    assert response.status_code == status.HTTP_200_OK
    updated = response.json()
    assert updated["title"] == "New"
    assert updated["author"] == "B"
