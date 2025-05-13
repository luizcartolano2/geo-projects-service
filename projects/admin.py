""" Docstring for the admin.py module.
"""
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Project model.
    This class allows filtering, searching, and displaying relevant project fields
    in the Django admin interface.
    """
    list_display = (
        "uuid", "name", "description", "start_date", "end_date",
        "status", "location", "latitude", "longitude"
    )
    search_fields = ("name", "location", "status")
    list_filter = ("status",)
