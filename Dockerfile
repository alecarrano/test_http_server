FROM python:3.8-slim-buster

WORKDIR /app

RUN sleep 161
COPY . .

CMD [ "python3", "app.py"]


