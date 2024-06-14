from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models, schemas

from database import get_db
from crud import ProductCrud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

v2_app = FastAPI()


# index
@v2_app.get("/")
def v2_index():
    """_summary_

    index de lApi
    """
    return ProductCrud.index()

# recuperer(lire) la liste de courses
@v2_app.get("/products", tags=["Product"], response_model=List[schemas.Product])
def get_products_list(element: Optional[str] = None,db: Session = Depends(get_db)):
    """_summary_

    recuperer la liste de tous les produits
    """
    try:
        return ProductCrud.get_list()
    except:
        raise HTTPException(status_code=404, detail="the required list is empty")

    
# ajouter un produit (un elt)a la liste
@v2_app.post("/add_product", tags=['Product'], response_model=schemas.Product, status_code=201)
def add_product_to_list(product_request: schemas.ProductCreate, db: Session = Depends(get_db)):
    """_summary_

    ajout d'un produit dans la liste
    """
    # chaque nouvel elt est unique par son id mais peut etre identique par les 
    # attributs ainsi pas de traitement sur existence de product

    return ProductCrud.add_to_list(db=db, new_product = product_request)

#supprimer un element de la liste elelment




# vider la liste



    

