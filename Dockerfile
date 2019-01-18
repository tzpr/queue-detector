# base image
FROM python:3.4-alpine

ADD redis-test.py /code
WORKDIR /code

# install packages
RUN pip install redis
RUN pip install schedule


CMD ["python", "redis-test.py"]