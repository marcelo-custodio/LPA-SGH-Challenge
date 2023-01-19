FROM python:3.10.9-slim-buster

WORKDIR /app
COPY . .

ENV MONGO_USER="plantinha-inteligente"
ENV MONGO_PWD="beP1jlt9lXIGuFYj"

RUN python3 -m pip install poetry
RUN python3 -m poetry config virtualenvs.create false
RUN python3 -m poetry install

ENTRYPOINT [ "python3", "app.py" ]