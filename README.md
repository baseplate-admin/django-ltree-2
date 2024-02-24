# django-ltree

[![Downloads](https://static.pepy.tech/badge/django-ltree-2)](https://pepy.tech/project/django-ltree-2)

A tree extension implementation to support hierarchical tree-like data in Django models,
using the native Postgres extension `ltree`.

Postgresql has already a optimized and very useful tree implementation for data.
The extension is [ltree](https://www.postgresql.org/docs/9.6/static/ltree.html)

This fork contains is a continuation of the work done by [`mariocesar`](https://github.com/mariocesar/) on [`django-ltree`](https://github.com/mariocesar/django-ltree) and merges the work done by [`simkimsia`](https://github.com/simkimsia) on [`greendeploy-django-ltree`](https://github.com/GreenDeploy-io/greendeploy-django-ltree)

<!--
[![Test](https://github.com/mariocesar/django-ltree/actions/workflows/test.yml/badge.svg)](https://github.com/mariocesar/django-ltree/actions/workflows/test.yml)
 -->

## Install

```py
pip install django-ltree
```

Then add `django_ltree` to `INSTALLED_APPS` in your Django project settings.

```python
INSTALLED_APPS = [
    ...,
    'django_ltree',
    ...
]
```

Then use it like this:

```python

from django_ltree.models import TreeModel


class CustomTree(TreeModel):
    ...

```

## Requires

-   Django 5.0 or superior
-   Python 3.10 or higher

