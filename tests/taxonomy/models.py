from django.db import models

from django_ltree.managers import TreeManager
from django_ltree.models import TreeModel


class Taxonomy(TreeModel):
    id: int
    name = models.TextField()

    def __str__(self):
        return f"{self.path}: {self.name}"


class TaxonomyName(TreeModel):
    id: int
    name = models.TextField()

    t_objects = TreeManager(path_field="name")
