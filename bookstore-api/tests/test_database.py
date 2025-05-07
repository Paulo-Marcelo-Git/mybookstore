# tests/test_database.py

from database import SessionLocal, get_db, engine
from sqlalchemy import text

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
