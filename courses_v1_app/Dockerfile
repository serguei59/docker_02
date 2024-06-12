FROM python:3.12-slim

WORKDIR . /courses_v1_app

COPY ./requirements.txt courses_v1_app/requirements.txt

RUN pip install -r requirements.txt

COPY . /courses_v1_app

CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]
