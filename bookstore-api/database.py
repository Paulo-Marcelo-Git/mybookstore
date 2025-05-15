# mybookstore/bookstore-api/database.py

import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Carrega variáveis de ambiente
env_file = os.getenv("ENV_FILE", ".env")
load_dotenv(dotenv_path=env_file)

def get_env_or_fail(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Variável de ambiente {var_name} não definida")
    return value

DB_USER = get_env_or_fail("DB_USER")
DB_PASS = quote_plus(get_env_or_fail("DB_PASS"))
DB_HOST = get_env_or_fail("DB_HOST")
DB_PORT = get_env_or_fail("DB_PORT")
DB_NAME = get_env_or_fail("DB_NAME")

if DB_NAME == ":memory:" or DB_NAME.endswith(".db"):
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}"
    connect_args = {"check_same_thread": False}
else:
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    connect_args = {"connect_timeout": 10}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
