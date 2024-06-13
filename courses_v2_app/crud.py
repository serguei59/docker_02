from sqlalchemy.orm import Session 
from . import models, schemas

class ProductCrud:


    # index
    def index():
        return {"Bienvenu(e) sur la version v2 de l'API liste de courses"}


    # recuperer(lire) la liste de courses
    # il faudrait faire un grouby en rajoutant une colonne avec les count par ligne

    def get_list(db: Session, skip: int = 0):
       return db.query(models.Product).offset(skip).all()

    # ajouter un produit (un elt)a la liste
    def add_to_list(db: Session, new_product = schemas.ProductCreate):
       db_product = models.Product(element=new_product.element, quantite=new_product.quantite, unite= new_product.unite)
       db.add(db_product)
       db.commit()
       db.refresh(db_product)
       return f"{db_product} a été ajouté à la liste de courses"
       
    #supprimer un element de la liste elelment
    def delete_from_list(db: Session, element: str):
    # si elt deja existant
        ##suppression de += unite
        ##suppression de += quantite

    #si non existant
        ##erreur


        pass


    # vider la liste
    def clear_list():
    #si liste existe
        ##vider la liste
    # sinon
        ##raise
        pass





