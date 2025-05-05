import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🚀 Troca aqui: carrega .env.test se definido via ENV_FILE
env_file = os.getenv("ENV_FILE", ".env")
load_dotenv(dotenv_path=env_file)

DB_USER = os.getenv("DB_USER")
DB_PASS = quote_plus(os.getenv("DB_PASS", ""))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# 🚀 Troca aqui: detecta se vai usar SQLite
if DB_NAME == ":memory:" or DB_NAME.endswith(".db"):
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}"
    connect_args = {"check_same_thread": False}
else:
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    connect_args = {}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
