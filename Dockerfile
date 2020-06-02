# Pull base image
FROM python:3.7-alpine
MAINTAINER Ata Ur Rehman
# Set environment variables
ENV PYTHONUNBUFFERED 1
# Set work directory
# Copy project
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user