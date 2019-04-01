FROM python:3.7-alpine

RUN apk update \
        && apk add --no-cache git openssh-client curl \
        gcc python3-dev postgresql-dev musl-dev \
        && pip install -U pipenv 

RUN mkdir -p /app/src
WORKDIR /app/src
