FROM node:8-alpine

RUN npm install -g sails
RUN npm install

WORKDIR /usr/src/app

ENTRYPOINT sails lift
