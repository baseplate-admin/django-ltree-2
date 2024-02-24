from collections import UserList
from django import forms
from django.core.validators import RegexValidator
from django.db.models.fields import TextField
from django.forms.widgets import TextInput

from collections.abc import Iterable
from typing import TypeVarTuple, NoReturn, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from django_ltree.models import TreeModel

path_label_validator = RegexValidator(
    r"^(?P<root>[a-zA-Z][a-zA-Z0-9_]*|\d+)(?:\.[a-zA-Z0-9_]+)*$",
    "A label is a sequence of alphanumeric characters and underscores separated by dots.",
    "invalid",
)


class PathValue(UserList[str]):
    def __init__(self, value: str | int | Iterable[str]):
        if isinstance(value, str):
            split_by = "/" if "/" in value else "."
            value = value.strip().split(split_by) if value else []
        elif isinstance(value, int):
            value = [str(value)]
        elif isinstance(value, Iterable):
            value = [str(v) for v in value]
        else:
            raise ValueError("Invalid value: {!r} for path".format(value))

        super().__init__(initlist=value)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return ".".join(self)


class PathValueProxy:
    def __init__(self, field_name: str) -> None:
        self.field_name = field_name

    def __get__(
        self, instance: "PathValueProxy | None", *args: TypeVarTuple
    ) -> "PathValueProxy" | "PathValue" | None:
        if instance is None:
            return self

        value = instance.__dict__[self.field_name]

        if value is None:
            return value

        return PathValue(instance.__dict__[self.field_name])

    def __set__(  # type: ignore
        self, instance: "PathValueProxy | None", value: str
    ) -> None | "PathValueProxy":
        if instance is None:
            return self

        instance.__dict__[self.field_name] = value


class PathFormField(forms.CharField):  # type: ignore
    default_validators = [path_label_validator]


class PathField(TextField):  # type: ignore
    default_validators = [path_label_validator]

    def db_type(self, *args: TypeVarTuple) -> str:
        return "ltree"

    def formfield(self, **kwargs: Any) -> Any:
        kwargs["form_class"] = PathFormField
        kwargs["widget"] = TextInput(attrs={"class": "vTextField"})
        return super().formfield(**kwargs)

    def contribute_to_class(
        self, cls: type["TreeModel"], name: str, private_only: bool = False
    ) -> None:
        super().contribute_to_class(cls, name)
        setattr(cls, self.name, PathValueProxy(self.name))

    def from_db_value(
        self, value: PathValue | "None", *args: TypeVarTuple
    ) -> PathValue | "None":
        if value is None:
            return value
        return PathValue(value)

    def get_prep_value(self, value: str | None) -> str | None:
        if value is None:
            return value
        return str(PathValue(value))

    def to_python(self, value: str | None | PathValue) -> PathValue | None:
        if value is None:
            return value
        elif isinstance(value, PathValue):
            return value

        return PathValue(value)

    def get_db_prep_value(
        self, value: str | None | PathValue, connection: str, prepared: bool = False
    ) -> str | None:
        if value is None:
            return value
        elif isinstance(value, PathValue):
            return str(value)
        elif isinstance(value, (list, str)):
            return str(PathValue(value))

        raise ValueError(f"Unknown value type {type(value)}")
