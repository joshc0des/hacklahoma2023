# syntax=docker/dockerfile:1

FROM python:3.8-alpine

EXPOSE 5000/tcp

WORKDIR /flaskapp

RUN apk update && apk add --no-cache git

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .