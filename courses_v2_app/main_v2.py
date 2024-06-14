from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn

from . import models, schemas

from .database import get_db, SessionLocal, engine
from .crud import ProductCrud


v2_app = FastAPI()

models.Base.metadata.create_all(bind=engine)

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
@v2_app.delete("/delete_product",tags=['Product'], response_model=schemas.Product, status_code=201)
def remove_from_list(product_request: schemas.ProductDelete, db:Session = Depends(get_db)):
    
    """_summary_

    retrait d' un produit de la liste à partie de son id
    """
    return ProductCrud.delete_from_list(db=db)


# vider la liste


#pour le executer du coup je dois le lancer 
if __name__== "__main__":
    uvicorn.run('courses_v2_app.main_v2:v2_app', port= 1234, reload=True)

    


    
# ceci est un module(cf __init__.py) a la racine du dossier
#  il faut le lancer en mode module dans le terminal depuis la racine(là dou il voit la situation)
# python3 -m courses_v2_app.main_v2
# (relative path separation points, suppression.py)
