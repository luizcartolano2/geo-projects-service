"""
Django Admin Configuration for Projects App

This module configures the Django admin interface for the Project model.
It customizes how projects are displayed, searched, and filtered in the admin panel.
"""
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Project model.

    Customizes the display and behavior of Projects in the Django admin with:
    - Optimized list display showing all relevant fields
    - Search functionality for key fields
    - Filtering capabilities by status
    - Automatic registration with the admin site

    Attributes:
        list_display (tuple): Fields to display in the project list view
        search_fields (tuple): Fields enabled for search functionality
        list_filter (tuple): Fields available for filtering the list
    """
    # Fields to display in the admin list view
    list_display = (
        "uuid", "name", "description", "start_date", "end_date",
        "status", "location", "latitude", "longitude"
    )

    # Fields enabled for search functionality
    search_fields = ("name", "location", "status")

    # Fields available for right-side filtering
    list_filter = ("status",)
