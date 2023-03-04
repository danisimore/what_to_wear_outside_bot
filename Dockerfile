FROM python:3.10-alpine

COPY requirements.txt /temp/requirements.txt
COPY what_to_wear_outside_bot /what_to_wear_outside_bot
WORKDIR /what_to_wear_outside_bot

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password wtwo-bot-adduser

USER wtwo-bot-adduser

