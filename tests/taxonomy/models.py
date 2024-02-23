from django.db import models

from django_ltree.models import TreeModel


class Taxonomy(TreeModel):
    name = models.TextField()

    def __str__(self):
        return f"{self.path}: {self.name}"
