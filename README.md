# Benzaiten

[![Build Status](https://api.travis-ci.org/polygon8/benzaiten.svg?branch=master)](https://travis-ci.org/polygon8/benzaiten)

Backend app for the Polygon 8 site

## Local setup

Requires Python 3.6x and Pipenv. [See here for help](https://djangoforbeginners.com/initial-setup/).

```
$ git clone https://github.com/polygon8/benzaiten.git
$ cd benzaiten
$ pipenv install
$ pipenv shell # activates the virtualenv
```

Set up the initial migration. Currently this is only for `users`.

```
$ python manage.py makemigrations users
$ python manage.py migrate
```

Create a superuser:

```
$ python manage.py createsuperuser
```

Run the app:

```
$ python manage.py runserver
```

Take a look: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Acknowledgments

This borrows heavily from [djangox](https://github.com/wsvincent/djangox).
