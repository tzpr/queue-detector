# Dockerfile for flask web api
# https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
# https://hub.docker.com/_/python/

# base image
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# run app when container starts
CMD [ "python", "app.py" ]