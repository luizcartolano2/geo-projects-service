"""
Projects App Configuration

This module contains the Django application configuration class for the 'projects' app.
It defines metadata and initialization settings for the projects application.
"""
from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    """
    Application configuration class for the projects app.

    This class configures application-specific settings including:
    - The default auto field type for models
    - The application name
    - Any application initialization behavior

    Attributes:
        default_auto_field (str): Specifies the default primary key field type
                                 to use for models that don't specify one.
        name (str): The full Python path to the application (e.g., 'projects').
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "projects"
