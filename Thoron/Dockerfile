FROM python:3.7-alpine

RUN apk update \
        && apk add --no-cache git openssh-client \
        && pip install -U pipenv 

# Creating working directory
RUN mkdir -p /app/src
WORKDIR /app/src

EXPOSE 8000

CMD pipenv install --system && python manage.py runserver
