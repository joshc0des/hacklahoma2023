# syntax=docker/dockerfile:1

FROM python:3.8-alpine

EXPOSE 5000/tcp

WORKDIR /flaskapp

COPY . /flaskapp

ENV FLASK_APP flaskapp

ENV AWS_REGION us-east-2

RUN apk update && apk add --no-cache git

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
