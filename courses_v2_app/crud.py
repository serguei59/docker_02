from sqlalchemy.orm import Session
from . import models, schemas

class ProductCrud:


    # index
    def index():
        return {"Bienvenu(e) sur la version v2 de l'API liste de courses"}

    
    # recuperer(lire) la liste de courses
    # il faudrait faire un grouby en rajoutant une colonne avec les count par ligne

    def get_list(db: Session, skip: int = 0, limit: int = 100):
       return db.query(models.Product).offset(skip).limit(limit).all()

    # ajouter un produit (un elt)a la liste
    def add_to_list(db: Session, new_product = schemas.ProductCreate):
       db_product = models.Product(element=new_product.element, quantite=new_product.quantite, unite= new_product.unite)
       #il faut verifier l unite si le produit existe deja=> a faire
       #product = session.query(models.Product).filter(.first)
       db.add(db_product)
       db.commit()
       db.refresh(db_product)
       return f"{db_product} a été ajouté à la liste de courses"
       
    #supprimer un element de la liste element à partir de son id
    def delete_from_list(db: Session, product_id= int):
        db_product = db.query(models.Product).filter_by(id=product_id).first()
        #verifier que le produit existe pour traiter sinon message d erreur=>a faire
        db.delete(db_product)
        db.commit()
        return f"{db_product} a été supprimé de la liste de courses"

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





