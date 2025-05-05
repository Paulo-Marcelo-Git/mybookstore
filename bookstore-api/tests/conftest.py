import os
import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base, engine, get_db  # agora importa get_db corretamente

# Cria todas as tabelas no banco definido (test.db ou :memory:)
Base.metadata.create_all(bind=engine)

# Override para usar o get_db real (que já conecta ao SQLite via .env.test)
app.dependency_overrides[get_db] = get_db

# Fixture do client com a app de teste
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
