from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from courses_v2_app import models, schemas
from courses_v2_app.database import get_db
from .crud import ProductCrud


courses_v2_app = FastAPI()




# index
@courses_v2_app.get("/")
def v2_index():
    """_summary_

    index de lApi
    """
    return ProductCrud.index()

# recuperer(lire) la liste de courses
@courses_v2_app.get("/products", tags=["Product"], response_model=List[schemas.Product])
def get_products_list(element: Optional[str] = None,db: Session = Depends(get_db)):
    """_summary_

    recuperer la liste de tous les produits
    """
    products_list = ProductCrud.get_list(db, Session)
    if len(products_list) == 0:
        return {"la liste est vide"}
    else:
        return {"content": products_list}
    
# ajouter un produit (un elt)a la liste





#supprimer un element de la liste elelment




# vider la liste



    

