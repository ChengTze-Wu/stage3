FROM python:3.7-slim
MAINTAINER chengtze

WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .