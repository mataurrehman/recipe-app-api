# Pull base image
FROM python:3.7-alpine
MAINTAINER Ata Ur Rehman
# Set environment variables
ENV PYTHONUNBUFFERED 1
# Set work directory
# Copy project
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user