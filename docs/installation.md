# Installation

## Requirements

-   Python 3.9 to 3.13 supported.
-   PyPy 3.9 to 3.10 supported.
-   Django 4.2 to 5.1 supported.
-   Postgres 14 to 17 supported.

## Installation

```{attention}
Please remember to uninstall `django-ltree` before installing `django-ltree-2`, since both uses `django_ltree` namespace.
```

1.  Install with **pip**:

```bash
python -m pip install django-ltree-2
```

2.  Add django-ltree to your `INSTALLED_APPS`:

```{code-block} python
:caption: settings.py

INSTALLED_APPS = [
    ...,
    "django_ltree",
    ...,
]
```

3.  Run migrations:

```sh
./manage.py migrate
```
