from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base

def test_engine_connection():
    # Verifica se consegue conectar ao banco e retornar uma conexão válida
    with engine.connect() as conn:
        assert conn.closed is False

def test_session_local():
    # Verifica se uma sessão pode ser criada e é instância de Session
    db = SessionLocal()
    try:
        assert isinstance(db, Session)
    finally:
        db.close()

def test_base_class():
    # Verifica se Base é uma classe declarativa funcional
    assert hasattr(Base, 'metadata')
