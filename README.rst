Demo Cookiecutter Django
===================
.. image:: https://img.shields.io/badge/Sponsor-Divelia-5b62ff.svg
    :target: https://divelia.com
    :alt: Documentation Status

.. image:: https://readthedocs.org/projects/cookiecutter-django/badge/?version=latest
    :target: https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

.. image:: https://img.shields.io/badge/version-0.0.3-34a853.svg
    :target: #
    :alt: Code style: black

* Codebase Django is a guide to boost ready-to-use Django code.
* Powered by Cookiecutter_.
* Thanks to Cristian_.

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Cristian: https://github.com/crisycochea

Features
---------

* For Django 3.0
* Works with Python 3.8
* Work with PostgreSQL 12.3, but customizable.
* Work with AWS
* Optimized development and production settings.
* 12-Factor_ based settings via django-environ_
* Secure by default. We believe in SSL.
* Optimized development and production settings
* Registration via django-allauth_ and dj-rest-auth_
* Comes with custom user model ready to go
* Media storage using Amazon S3 or Google Cloud Storage
* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)

Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Serve static files from Amazon S3
* Configuration for Celery_ and Flower_ (the latter in Docker setup only)

.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _django-allauth: https://github.com/pennersr/django-allauth
.. _dj-rest-auth: https://github.com/iMerica/dj-rest-auth
.. _Celery: http://www.celeryproject.org/
.. _Flower: https://github.com/mher/flower
.. _docker-compose: https://github.com/docker/compose
.. _Traefik: https://traefik.io/
.. _LetsEncrypt: https://letsencrypt.org/


Constraints
-----------

* Only available for AWS.
* Only maintained 3rd party libraries are used.
* Uses PostgreSQL everywhere (11.8 - 12.3)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).

Development
-----------
* I will try to update and improve this codebase as I learn more. To get started on this project, I recommend you check out the Django, Cookiecutter pydanny documentation on how to make this project run locally. If you don't want to, just run:


