FROM python:latest

RUN apt-get update
RUN apt-get install -y ssdeep

RUN pip install celery[redis]
RUN pip install elasticsearch
RUN pip install fastapi
RUN pip install uvicorn

WORKDIR /src
COPY . /src/