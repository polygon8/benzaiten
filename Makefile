SHELL := /bin/bash

install:
	pip install pipenv
	pipenv lock
	pipenv install --dev

lint:
	pipenv run flake8

migrate:
	pipenv run ./manage.py migrate

runserver:
	pipenv run ./manage.py runserver

test:
	pipenv run ./manage.py test
