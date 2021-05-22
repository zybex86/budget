FROM python:3.8-alpine

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -U pip
RUN pip install -r /requirements.txt
RUN apk del .tmp-build

RUN mkdir /budget
WORKDIR /budget
COPY ./budget /budget

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

USER user
