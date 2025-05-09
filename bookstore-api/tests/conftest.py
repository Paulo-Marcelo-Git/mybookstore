# mybookstore\bookstore-api\tests\conftest.py

import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from main import app
from database import Base, engine, get_db

# Cria todas as tabelas antes dos testes
@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Override do get_db para usar a sessão real definida no app
app.dependency_overrides[get_db] = get_db

# Fixture do client para os testes FastAPI
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
