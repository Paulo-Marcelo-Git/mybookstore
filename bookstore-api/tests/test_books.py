import pytest

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API está no ar!"}

def test_create_book(client):
    payload = {"title": "Clean Code", "author": "Robert C. Martin", "description": "Código limpo."}
    response = client.post("/books/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Clean Code"
    assert "id" in data

def test_list_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_book_not_found(client):
    response = client.get("/books/999999")
    assert response.status_code == 404

def test_update_book(client):
    # Cria primeiro
    new_book = client.post("/books/", json={"title": "Old", "author": "A", "description": "desc"}).json()
    update_payload = {"title": "New", "author": "B", "description": "Updated"}
    response = client.put(f"/books/{new_book['id']}", json=update_payload)
    assert response.status_code == 200
    assert response.json()["title"] == "New"

def test_delete_book(client):
    new_book = client.post("/books/", json={"title": "To delete", "author": "X", "description": ""}).json()
    response = client.delete(f"/books/{new_book['id']}")
    assert response.status_code == 200
    assert response.json() == {"ok": True}
