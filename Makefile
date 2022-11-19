POSTGRES_USER := commsquare
POSTGRES_PASSWORD := commsquare
POSTGRES_DB := commsquare
DOCKER_SERVER_IMAGE_TAG := commsquare

SHELL := /bin/bash

clean:
	sudo rm -rf venv

venv:
	python3 -m venv venv
	source venv/bin/activate && pip3 install --upgrade pip
	source venv/bin/activate && pip3 install -r requirements.txt

run:
	source venv/bin/activate && python3 manage.py makemigrations && python3 manage.py migrate
	source venv/bin/activate && python3 manage.py runserver