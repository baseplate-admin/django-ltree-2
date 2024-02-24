from django.db.models import Transform
from django.db.models import fields
from .fields import PathField


__all__ = ("NLevel",)


@PathField.register_lookup
class NLevel(Transform):  # type: ignore
    lookup_name = "depth"
    function = "nlevel"

    @property
    def output_field(self) -> fields.IntegerField:
        return fields.IntegerField()
