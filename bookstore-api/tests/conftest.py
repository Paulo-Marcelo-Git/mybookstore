# mybookstore\bookstore-api\tests\conftest.py

import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from main import app
from database import Base, engine, get_db

# Prepara banco antes e depois dos testes
@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Override dependency
app.dependency_overrides[get_db] = get_db

# Cliente FastAPI fixture
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
