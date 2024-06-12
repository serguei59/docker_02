from fastapi import FastAPI, HTTPException
import uvicorn




courses_v1_app = FastAPI()

ma_liste_de_courses = [
    {"element": "farine", "quantite": 200, "unite": "grammes"},
    {"element": "oeuf", "quantite": 6, "unite": "unite"}
]

mon_dictionnaire_de_courses = {
    "farine":[200,"grammes"], 
    "oeuf":[6,"unite"]
}

@courses_v1_app.get("/")
def index():
    return {"bonjour, bienvenu sur l' API liste de courses"}

###

@courses_v1_app.get("/get_liste")
def get_list():
    if len(ma_liste_de_courses) == 0:
        return {"la liste est vide"}
    else:
        return {"content": ma_liste_de_courses}
    
@courses_v1_app.get("/get_dictionnaire")
def get_dictionnaire():
    if len(mon_dictionnaire_de_courses) == 0:
        return {"le dictionnaire est vide"}
    else:
        return {"content": mon_dictionnaire_de_courses}
    
###
""" 
ma_liste_de_courses = [
    {"element":"farine","quantite":200,"unite":"grammes"},
    {"element":"oeuf","quantite":6,"unite":"unite"}
] """
  
@courses_v1_app.post("/add_to_list")
def add_to_list(element:str, quantite:int, unite:None|str=None):
     print(ma_liste_de_courses)
     #verififier si l élément dans la liste(est dans les cles de mon dictionnaire)
     ma_liste_de_comprehension = [dico["element"] for dico in ma_liste_de_courses]
     print(ma_liste_de_comprehension)
     print(type(ma_liste_de_comprehension))
     if element in ma_liste_de_comprehension:
        index_element = ma_liste_de_comprehension.index(element)
        print(index_element)
        if unite:
            #si oui verifier si l unite est la meme
            if unite == ma_liste_de_courses[index_element]["unite"]:
                #si l unite est la meme on ajoute les quantités
                ma_liste_de_courses[index_element]["quantite"] += quantite
                return {"content":ma_liste_de_courses[index_element]}
            # si non renvoi d un messsage d erreur
            else:
                raise HTTPException(status_code=400,
                                detail=f"not the good unit for element, {element} is in {ma_liste_de_courses[index_element]}")
        # pas d unite fournie j ajoute par defaut
        else:
            ma_liste_de_courses[index_element]["quantite"] += quantite
            return {"content":ma_liste_de_courses[index_element]}
     #si pas trouvé ajout de l elet à la liste
     else:
        ma_liste_de_courses.append(
            {"element":element,
             "quantite":quantite,
             "unite":unite}

        )
        return {"content":ma_liste_de_courses[-1]}
""" 
mon_dictionnaire_de_courses = {
    "farine":[200,"grammes"],
    "oeuf":[6,"unité"]
} """

@courses_v1_app.post("/add_to_dictionnaire")
def add_to_dictionnaire(element:str, quantite:int, unite:None|str=None):
    #verififier si l élément dans le dictionnaire(est dans les cles de mon dictionnaire)
    if element in mon_dictionnaire_de_courses:
        if unite:
            #si oui verifier si l unite est la meme
            if unite == mon_dictionnaire_de_courses[element][1]:
                #si l unite est la meme on ajoute les quantités
                mon_dictionnaire_de_courses[element][0] += quantite
                return {element:mon_dictionnaire_de_courses[element]}
            # si non renvoi d un messsage d erreur
            else:
                raise HTTPException(status_code=400,
                                detail=f"not the good unit for element, {element} is in {mon_dictionnaire_de_courses[element][1]}")
        # pas d unite fournie j ajoute par defaut
        else:
            mon_dictionnaire_de_courses[element][0] += quantite
            return {element:mon_dictionnaire_de_courses[element]}
    #si pas trouvé ajout de l elet au dictionnaire
    else:
        mon_dictionnaire_de_courses[element] = [quantite,unite]
        return {element:mon_dictionnaire_de_courses[element]}

###
"""
ma_liste_de_courses = [
    {"element":"farine","quantite":200,"unite":"grammes"},
    {"element":"oeuf","quantite":6,"unite":"unite"}
]
"""

@courses_v1_app.delete("/delete_from_liste") 
def remove_from_list(element:str, quantite:int, unite:None|str=None): 
      #verififier si l élément dans la liste(est dans les cles de mon dictionnaire)
     ma_liste_de_comprehension = [dico["element"] for dico in ma_liste_de_courses]
     if element in ma_liste_de_comprehension:
        index_element = ma_liste_de_comprehension.index(element)
        if unite:
            #si oui verifier si l unite est la meme
            if unite == ma_liste_de_courses[index_element]["unite"]:
                #si l unite est la meme on déduit les quantités
                ma_liste_de_courses[index_element]["quantite"] -= quantite
                return {"content":ma_liste_de_courses[index_element]}
            # si non renvoi d un messsage d erreur
            else:
                raise HTTPException(status_code=400,
                                detail=f"not the good unit for element, {element} is in {ma_liste_de_courses[index_element]}")
        # pas d unite fournie je supprimme par defaut
        else:
            ma_liste_de_courses[index_element]["quantite"] -= quantite
            return {"content":ma_liste_de_courses[index_element]}
     #si pas trouvé dans la liste retour message erreur lequel +quelle exception+quel code status?
     else:
        raise HTTPException(status_code=400,
                            detail=f"{element} doesn't exist in {ma_liste_de_courses}")
"""
    try: 
        ma_liste_integer.remove(element) 
        return {"content": ma_liste_integer} 
    except ValueError: 
        raise HTTPException(status_code=404, detail="Element not found in the list")  
    

     

          

mon_dictionnaire_de_courses = {
    "farine":[200,"grammes"],
    "oeuf":[6,"unité"]
    }
    """

#

@courses_v1_app.delete("/delete_from_dictionnaire") 
def remove_from_dictionnaire(element:str, quantite:int, unite:None|str=None):
    #verififier si l élément dans le dictionnaire(est dans les cles de mon dictionnaire)
    if element in mon_dictionnaire_de_courses:
        if unite:
            #si oui verifier si l unite est la meme
            if unite == mon_dictionnaire_de_courses[element][1]:
                #si l unite est la meme on supprimme les quantités
                mon_dictionnaire_de_courses[element][0] -= quantite
                return {element:mon_dictionnaire_de_courses[element]}
            # si non renvoi d un messsage d erreur
            else:
                raise HTTPException(status_code=400,
                                detail=f"not the good unit for element, {element} is in {mon_dictionnaire_de_courses[element][1]}")
        # pas d unite fournie je supprime par defaut
        else:
            mon_dictionnaire_de_courses[element][0] += quantite
            return {element:mon_dictionnaire_de_courses[element]}
    #si pas trouvé message erreur
    else:
        raise HTTPException(status_code=400,
                            detail=f"{element} doesn't exist in {mon_dictionnaire_de_courses}")
   

@courses_v1_app.delete("/clean_liste")          
def clean_liste():
    try:
        ma_liste_de_courses.clear()
        return {"liste videe":ma_liste_de_courses}
    except:
        raise HTTPException(status_code=400,
                            detail=f"bad request")

    
    
@courses_v1_app.delete("/clean_dictionnaire")
def clean_dictionnaire():
    try:
        mon_dictionnaire_de_courses.clear()
        return {"dictionnaire vidé":mon_dictionnaire_de_courses}
    except:
        raise HTTPException(status_code=400,
                            detail=f"bad request")
          
              


#uvicorn main:app --reload


