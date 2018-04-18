SHELL := /bin/bash

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
