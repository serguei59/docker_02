from fastapi import FastAPI, HTTPException


courses_v2_app = FastAPI()

mon_dictionnaire_de_courses = {
    "farine":[200,"grammes"], 
    "oeuf":[6,"unite"]
}

@courses_v2_app.get("/")
def index():
    return {"bonjour, bienvenu sur l' API liste de courses"}

@courses_v2_app.get("/get_dictionnaire")
def get_dictionnaire():
    if len(mon_dictionnaire_de_courses) == 0:
        return {"le dictionnaire est vide"}
    else:
        return {"content": mon_dictionnaire_de_courses}
    

