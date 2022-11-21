FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

COPY . .
