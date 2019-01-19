# Dockerfile for node.js Slack api
# https://nodejs.org/en/docs/guides/nodejs-docker-webapp/

# base image
FROM node:8

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm install --only=production

# Bundle app source
COPY . .

EXPOSE 4390
CMD [ "node", "app.js" ]