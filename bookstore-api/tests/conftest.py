import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient
from main import app
from database import Base
import database  # Para usar o get_db original

# URL do SQLite temporário para testes
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

# Cria o engine e session local só para testes
engine_test = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Cria as tabelas no SQLite
Base.metadata.create_all(bind=engine_test)

# Override da dependência get_db para usar o SQLite nos testes
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[database.get_db] = override_get_db

# Fixture para injetar o TestClient com SQLite
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
