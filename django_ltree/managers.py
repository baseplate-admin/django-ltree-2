from django.db import models
from typing import TYPE_CHECKING
from django_ltree.paths import PathGenerator

from .querysets import TreeQuerySet

if TYPE_CHECKING:
    from django_ltree.models import TreeModel


class TreeManager(models.Manager["TreeModel"]):
    def get_queryset(self) -> TreeQuerySet:
        """Returns a queryset with the models ordered by `path`"""

        return TreeQuerySet(model=self.model, using=self._db).order_by("path")

    def roots(self) -> TreeQuerySet:
        """Returns the roots of a given model"""

        return self.filter().roots()

    def children(self, path: str) -> TreeQuerySet:
        """Returns the childrens of a given object"""

        return self.filter().children(path)

    def create_child(self, parent: "TreeModel | None" = None, **kwargs) -> "TreeModel":
        """Creates a tree child with or without parent"""

        paths_in_use = parent.children() if parent else self.roots()
        prefix = parent.path if parent else None
        path_generator = PathGenerator(
            prefix,
            skip=paths_in_use.values_list("path", flat=True),
        )
        kwargs["path"] = path_generator.next()
        return self.create(**kwargs)
