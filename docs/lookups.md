# Lookups

`django-ltree` provides several custom lookups to interact with the ltree path efficiently using PostgreSQL operators.

Assume we have the following model and data:

```{code-block} python
from django.db import models
from django_ltree.fields import PathField

class Taxonomy(models.Model):
    path = PathField()
    name = models.CharField(max_length=100)

# Data
Taxonomy.objects.create(path="tenant_a", name="Tenant A")
Taxonomy.objects.create(path="tenant_a.departments", name="Departments")
Taxonomy.objects.create(path="tenant_a.departments.hr", name="HR")
Taxonomy.objects.create(path="tenant_a.departments.alpha", name="Alpha Project")
Taxonomy.objects.create(path="shared.public.docs", name="Public Docs")
```

## exact

The default lookup for equality. Corresponds to the `=` operator.

```{code-block} python
Taxonomy.objects.filter(path__exact="tenant_a.departments.hr")
```

## ancestors

Finds objects that are ancestors of the given path (or equal to it). Corresponds to the `@>` operator.
This is useful to find the "breadcrumb" path for a specific node.

```{code-block} python
# Returns "Tenant A", "Departments" (if filtered by ancestors of 'tenant_a.departments.hr')
# To get the breadcrumb path to HR:
Taxonomy.objects.filter(path__ancestors="tenant_a.departments.hr")
```

## descendants

Finds objects that are descendants of the given path (or equal to it). Corresponds to the `<@` operator.
This is useful to find all children/grandchildren of a node.

```{code-block} python
# Returns "HR", "Alpha Project", "Departments"
Taxonomy.objects.filter(path__descendants="tenant_a.departments")
```

## match

Performs ltree pattern matching using lqueries. Corresponds to the `~` operator.
You can use wildcards like `*`.

```{code-block} python
# Match all descendants of tenant_a.departments
Taxonomy.objects.filter(path__match="tenant_a.departments.*")
```

## contains

Checks if the path matches **any** of the lqueries in a list. Corresponds to the `?` operator.
This requires passing a list or tuple of lquery patterns.

```{code-block} python
patterns = [
    "tenant_a.departments.*",
    "shared.public.*",
]
# Allows filtering by multiple subtrees at once.
# Matches both 'tenant_a.departments.hr' and 'shared.public.docs'
Taxonomy.objects.filter(path__contains=patterns)
```
