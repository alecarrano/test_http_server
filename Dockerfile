FROM python:3.8-slim-buster

WORKDIR /app

RUN python -m pip install psycopg2

ARG QOVERY_PROJECT_ID

COPY . .

CMD [ "python3", "app.py"]


