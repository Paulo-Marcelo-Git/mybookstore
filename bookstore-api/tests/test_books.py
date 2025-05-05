import pytest

def test_health_check(client):
    """Verifica se o endpoint raiz responde com status 200"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API está no ar!"}  # se seu endpoint '/' retorna algo assim
