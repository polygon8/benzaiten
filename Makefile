SHELL := /bin/bash

bootstrap: create_db install migrate

create_db:
	psql -c 'create database benzaiten;' -U postgres

install:
	pip install pipenv
	pipenv lock
	pipenv install --dev

lint:
	pipenv run flake8

migrate:
	pipenv run ./manage.py migrate

requirements:
	pipenv lock -r > ./requirements.txt
	pipenv lock -r --dev > ./requirements-dev.text

runserver:
	pipenv run ./manage.py runserver

test:
	pipenv run pytest
