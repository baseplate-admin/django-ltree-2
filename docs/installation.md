# Installation

## Requirements

Python 3.8 to 3.12 supported.

Django 4.2 to 5.0 supported.

## Installation

1.  Install with **pip**:

    ``` sh
    python -m pip install django-ltree-2
    ```

2.  Add django-ltree to your `INSTALLED_APPS`:

    ``` python
    # settings.py
    INSTALLED_APPS = [
        ...,
        "django_ltree",
        ...,
    ]
    ```

3.  Run migrations:

    ``` sh
    ./manage.py migrate
    ```
