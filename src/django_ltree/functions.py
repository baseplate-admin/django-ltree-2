from django.db.models import fields
from django.db.models.expressions import Func

from .fields import PathField

__all__ = ("NLevel", "Subpath")


class NLevel(Func):
    function = "NLEVEL"
    arity = 1

    @property
    def output_field(self):
        return fields.IntegerField()


class Subpath(Func):
    function = "SUBPATH"
    output_field = PathField()

    def __init__(self, *expressions, output_field=None, **extra):
        if len(expressions) != 2 and len(expressions) != 3:
            raise ValueError("Subpath takes either 2 or 3 arguments")
        super().__init__(*expressions, output_field=output_field, **extra)
