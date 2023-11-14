from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///../users.db"  # Use SQLite for simplicity

#database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
#database.bind_to(engine)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db. close()
