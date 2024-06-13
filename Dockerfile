FROM python:3.12-slim

WORKDIR /courses_v2_app

COPY ./requirements.txt /courses_v2_app/requirements.txt

RUN pip install -r requirements.txt

COPY . /courses_v2_app

CMD ["uvicorn","main_v2:courses_v2_app", "--host", "0.0.0.0", "--port", "8000"]