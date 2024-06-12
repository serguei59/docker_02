from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create database url for sqlAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./courses_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#create sqlAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#creation de l instance de Session via methoe sessionmaker == la databse session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creation de la Base classe
Base = declarative_base()

