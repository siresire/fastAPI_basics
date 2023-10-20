from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Define the database url 
SQLALCHEMY_DATABASE_URL = "sqlite:///blog.db"

# Creating the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#  define sessionlocal, sessionmaker is a class that will allow us to create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()