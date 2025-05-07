import pytest

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API está no ar!"}

def test_create_book(client):
    payload = {"title": "Clean Code", "author": "Robert C. Martin", "description": "Código limpo."}
    response = client.post("/books/", json=payload)
    assert response.status_code == 201  # Correto para POST
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert "id" in data
    assert "create_date" in data
    assert "update_date" in data

def test_list_books(client):
    # Cria um livro para garantir que não volte vazio
    client.post("/books/", json={"title": "Livro 1", "author": "Autor 1", "description": ""})
    response = client.get("/books/")
    assert response.status_code == 200
    livros = response.json()
    assert isinstance(livros, list)
    assert any("title" in livro for livro in livros)

def test_read_book_not_found(client):
    response = client.get("/books/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Livro não encontrado"

def test_update_book(client):
    # Cria o livro
    new_book = client.post("/books/", json={"title": "Old", "author": "A", "description": "desc"}).json()
    update_payload = {"title": "New", "author": "B", "description": "Updated"}
    response = client.put(f"/books/{new_book['id']}", json=update_payload)
    assert response.status_code == 200
    updated = response.json()
    assert updated["title"] == "New"
    assert updated["author"] == "B"
    assert "update_date" in updated

def test_delete_book(client):
    new_book = client.post("/books/", json={"title": "To delete", "author": "X", "description": ""}).json()
    response = client.delete(f"/books/{new_book['id']}")
    assert response.status_code == 204
    assert response.content == b''

    # Garante que foi realmente deletado
    response = client.get(f"/books/{new_book['id']}")
    assert response.status_code == 404
