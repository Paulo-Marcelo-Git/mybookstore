# tests/test_database.py

import os
import pytest
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from database import SessionLocal, get_db, engine
from importlib import reload
import database


def test_get_db_yields_session():
    gen = get_db()
    db = next(gen)
    assert db is not None
    assert hasattr(db, "commit")
    assert hasattr(db, "execute")
    gen.close()  # finaliza o generator para passar pelo finally


def test_engine_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_session_local_instance():
    db = SessionLocal()
    assert db.bind == engine
    db.close()


def test_get_env_or_fail_raises(monkeypatch):
    monkeypatch.delenv("FAKE_ENV_VAR", raising=False)
    with pytest.raises(ValueError, match="Variável de ambiente FAKE_ENV_VAR não definida"):
        get_env_or_fail("FAKE_ENV_VAR")


def test_reload_database_module_with_invalid_db(monkeypatch):
    monkeypatch.setenv("DB_NAME", "")  # força erro de retorno vazio
    monkeypatch.setenv("DB_USER", "x")
    monkeypatch.setenv("DB_PASS", "x")
    monkeypatch.setenv("DB_HOST", "x")
    monkeypatch.setenv("DB_PORT", "x")
    with pytest.raises(ValueError, match="Variável de ambiente DB_NAME não definida"):
        reload(database)
