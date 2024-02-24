from django.apps import AppConfig


class DjangoLtreeConfig(AppConfig):  # type: ignore
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_ltree"

    def ready(self) -> None:
        from . import checks as checks
        from . import lookups as lookups
        from . import functions as functions
