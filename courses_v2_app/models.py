from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    element = Column(String, unique=True, index=True)
    quantite = Column(Integer)
    unite = Column(String, default=True)
    

#creer une classe Liste de courses(Products?)?
#attribut owner element quantite fixeecomme la somme des quantites pour cet element
# unite comme somme des unites pour cet element