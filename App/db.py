from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///./todo_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False},
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class DBContext:
    def __init__(self):
        self.db = Session()

    def __enter__(self):
        return self.db

    def __exit__(self, et, ev, tb):
        self.db.close()