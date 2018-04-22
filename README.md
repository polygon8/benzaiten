# Benzaiten

[![Build Status](https://api.travis-ci.org/polygon8/benzaiten.svg?branch=master)](https://travis-ci.org/polygon8/benzaiten)

Backend app for the Polygon 8 site

## Local setup

Requires Python 3.6x and pip. [See here for help](https://djangoforbeginners.com/initial-setup/).

Also needs a running [postgres server](https://wiki.postgresql.org/wiki/Detailed_installation_guides).

```
$ git clone https://github.com/polygon8/benzaiten.git
$ cd benzaiten
$ make bootstrap
$ pipenv shell # activates the virtualenv
```

Run the app:

```
$ make runserver
```

You can create a super user if you like, but for the purposes of interacting with the app itself it is not necessary:

```
$ python manage.py createsuperuser
```

Take a look: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Run the tests:

```
$ make test
```

## Acknowledgments

This borrows heavily from [djangox](https://github.com/wsvincent/djangox).
