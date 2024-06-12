from fastapi import FastAPI, HTTPException
import uvicorn
ma_liste_de_courses = [
    {"element":"farine","quantite":200,"unite":"grammes"},
    {"element":"oeuf","quantite":6,"unite":"unite"}
]

mon_dictionnaire_de_courses = {
    "farine":[200,"grammes"],
    "oeuf":[6,"unite"]
}

app = FastAPI()

@app.get("/")
def index():
    return {"bonjour, bienvenu sur l' API liste de courses"}

@app.get("/get_liste")
def get_list():
    if len(mon_dictionnaire_de_courses)>0:
        return {"content": mon_dictionnaire_de_courses}
    else:
        return {"la liste est vide"}
    
  
@app.post("/liste")
def add_to_list(item):
    mon_dictionnaire_de_courses.append(item)
    return {"content": mon_dictionnaire_de_courses}

mon_dictionnaire_de_courses = {
    "farine":[200,"grammes"],
    "oeuf":[6,"unité"]
}

@app.post("/add_to_dictionnaire")
def add_to_dictionnaire(element:str, quantite:int, unite:None|str=None):
    #verififier si l élément dans le dictionnaire(est dans les cles de mon dictionnaire)
    if element in mon_dictionnaire_de_courses:
        if unite:
            #si oui verifier si l unite est la meme
            if unite == mon_dictionnaire_de_courses["farine"][1]:
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

ma_liste_de_courses = [
    {"element":"farine","quantite":200,"unite":"grammes"},
    {"element":"oeuf","quantite":6,"unite":"unite"}
]

@app.post("add_to_list")
def add_to_list(element: str, quantite:int, unite:None|str=None):
     #verififier si l élément dans la liste(est dans les cles de mon dictionnaire)
     ma_liste_de_comprehension = [dico["element"] for dico in ma_liste_de_courses]
     if element in ma_liste_de_comprehension:
        index_element = ma_liste_de_courses.index(element)
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
        
#uvicorn main:app --reload

"""

@app.delete("/liste") 
def remove_from_list(element: int): 
    try: 
        ma_liste_integer.remove(element) 
        return {"content": ma_liste_integer} 
    except ValueError: 
        raise HTTPException(status_code=404, detail="Element not found in the list")  """

