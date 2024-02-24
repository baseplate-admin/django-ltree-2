Installation
============

Requirements
------------

Python 3.10 to 3.12 supported.

Django 4.2 to 5.0 supported.


Installation
------------

1. Install with **pip**:

   .. code-block:: sh

       python -m pip install django-ltree-2

2. Add django-ltree to your ``INSTALLED_APPS``:

   .. code-block:: python

       INSTALLED_APPS = [
           ...,
           "django_ltree",
           ...,
       ]

3. Run migrations:

   .. code-block:: sh
    
        ./manage.py migrate