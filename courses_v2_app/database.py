from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create database url for sqlAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/courses_app_v2.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#create sqlAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#creation de l instance de Session via methoe sessionmaker == la databse session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creation de la Base classe dont nos les database models ou classes heriterons
Base = declarative_base()

#get_db can be used to create independent database session for each request
# yield is used to create a database session for each request. 
# Close it after finishing the request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()