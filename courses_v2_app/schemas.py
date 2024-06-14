from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    id: int
    element: str
    quantite: int
    #unite: str | None = None
    unite: Optional[str] = None

class ProductCreate(ProductBase):
   element: str
   quantite: int
    #unite: str | None = None
   unite: Optional[str] = None
   
    
class ProductDelete(ProductBase):
    id: int

class Product(ProductBase):
    id: int
    element: str


    class config:
        orm_mode = True
