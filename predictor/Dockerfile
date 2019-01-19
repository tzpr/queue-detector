# Dockerfile for flask web api
FROM python:3.6.3

ENV BIND_PORT 5000
ENV REDIS_HOST localhost
ENV REDIS_PORT 6379

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY . .

EXPOSE $BIND_PORT

CMD [ "python", "app.py" ]