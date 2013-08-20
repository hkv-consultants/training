Summary day 1
===================

#. Create `GitHub <https://www.github.com>`_ account and repository `<project_name>`.

#. Install GitHub client and clone repository.

#. Start Django project::

       manage.py startproject <project_name>

#. Configure database in project settings in `<repo_root>/<project_name>/<project_name>/settings.py`.

#. Test development server on `http://127.0.0.1:8000/`::

       manage.py runserver

#. Start Django app::

       manage.py startapp <app_name>

#. Create `models <https://docs.djangoproject.com/en/dev/ref/models/instances/>`_ ('tables') in `<repo_root>/<project_name>/<app_name>/models.py`

#. Create tables and database::

       manage.py syncdb

#. Setup `Django admin <https://docs.djangoproject.com/en/1.5/ref/contrib/admin/>`_ and enter initial data.

#. Explore `Python/Django shell <https://docs.djangoproject.com/en/dev/ref/django-admin/#shell>`_, using IPython.

#. Explore `logging of generated SQL <http://dabapps.com/blog/logging-sql-queries-django-13/>`_.

#. Explore basic `QuerySet usage <https://docs.djangoproject.com/en/dev/topics/db/queries/>`_ and `aggregates <https://docs.djangoproject.com/en/dev/topics/db/aggregation/>`_ in shell.

#. Configure Django admin filters and model `__unicode__ <https://docs.djangoproject.com/en/dev/ref/models/instances/#unicode>`_ representation.

#. Construct `function based view <https://docs.djangoproject.com/en/dev/topics/http/views/>`_ and map to it from (unparametrized) URL.

#. Create base and view-specific template and render basic list template.

#. Introduce `class-based (generic) views <http://georgebrock.github.io/talks/intro-to-class-based-generic-views/>`_.
