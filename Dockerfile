FROM python:3.12-slim
#je cree un dossier courses_v2app dans mon container
RUN mkdir -p /courses_v2_app

# copy demande un chemin absolu je pars de la racine
COPY ./requirements.txt /courses_v2_app/requirements.txt

RUN pip install -r courses_v2_app/requirements.txt

RUN pip install fastapi uvicorn sqlalchemy

COPY ./courses_v2_app /courses_v2_app

CMD ["uvicorn","courses_v2_app.main_v2:v2_app", "--host", "0.0.0.0", "--port", "8000"]