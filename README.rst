HKV Django Training
====================

Getting started
---------------
#. Make sure `VirtualEnv and PIP <http://docs.python-guide.org/en/latest/starting/install/win/#distribute-pip>`_ are installed.
#. Create a virtual environment::

       virtualenv env

#. Activate the environment::

       venv\Scripts\activate.bat

#. Install requirements from `requirements.txt`::

       pip install -r requirements.txt

#. Create a database::

       python manage.py syncdb

#. Run the development server::

       python manage.py runserver

#. Open the app in the browser at http://127.0.0.1:8000/


Preparatory material
---------------------
* `Crash into Python <http://stephensugden.com/crash_into_python/>`_
* `Writing your first Django app (tutorial) <https://docs.djangoproject.com/en/1.5/intro/>`_
* `Getting started with Django <https://github.com/dokterbob/django-getting-started>`_

Summaries
----------
* `Day 1 <https://github.com/hkv-consultants/training/blob/master/summary_day1.rst>`_
* `Day 2 <https://github.com/hkv-consultants/training/blob/master/summary_day2.rst>`_

Reference material
-------------------
* `Hitchhiker's Guide to Python <http://docs.python-guide.org/en/latest/index.html>`_
* `Two Scoops of Django <https://django.2scoops.org/>`_
* `Official Django documentation <https://docs.djangoproject.com/en/1.5/>`_
* `Official Python documentation <http://docs.python.org/2/>`_
