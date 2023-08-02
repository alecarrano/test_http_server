FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 simple-websocket-server grpcio-tools
    

ARG QOVERY_PROJECT_ID

COPY . .

CMD [ "python3", "app.py"]


