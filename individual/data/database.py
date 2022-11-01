import os

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import BASE_DIR

print("BASE", BASE_DIR)

DATABASE_URL = os.path.join(BASE_DIR, config('DATABASE_NAME'))
SQLALCHEMY_DATABASE_URL = f'sqlite:///{DATABASE_URL}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
