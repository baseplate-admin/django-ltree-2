from django.apps import AppConfig


def register_pathfield():
    # Register field checks, lookups and functions
    from . import checks as checks
    from . import lookups as lookups
    from . import functions as functions


class DjangoLtreeConfig(AppConfig):
    name = "django_ltree"

    def ready(self):
        register_pathfield()
