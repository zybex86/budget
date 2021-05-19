FROM python:3.8-alpine

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -U pip
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./budget /app

RUN adduser -D user
USER user
