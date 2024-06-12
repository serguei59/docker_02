from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    element = Column(String, unique=True, index=True)
    quantite = Column(Integer)
    unite = Column(String, default=True)