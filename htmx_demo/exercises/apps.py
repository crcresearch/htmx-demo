"""App configuration for exercises."""

from django.apps import AppConfig


class ExercisesConfig(AppConfig):
    """Configuration for the exercises app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "htmx_demo.exercises"
    verbose_name = "HTMX Exercises"

