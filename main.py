from fastapi import FastAPI, HTTPException

mon_dictionnaire_de_courses = {}

app = FastAPI()

@app.get("/")
def index():
    return {"bonjour, bienvenu sur l' API liste de courses"}

@app.get("/liste")
def get_list():
    if len(mon_dictionnaire_de_courses)>0:
        return {"content": len(mon_dictionnaire_de_courses)}
    else:
        return {"la liste est vide"}
    
"""   
@app.post("/liste")
def add_to_list(element:):
    ma_liste_integer.append(element)
    return {"content": ma_liste_integer}



@app.delete("/liste") 
def remove_from_list(element: int): 
    try: 
        ma_liste_integer.remove(element) 
        return {"content": ma_liste_integer} 
    except ValueError: 
        raise HTTPException(status_code=404, detail="Element not found in the list")  """


#  uvicorn main:app --reload