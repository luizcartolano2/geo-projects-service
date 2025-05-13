""" Docstring for the models.py module.
"""
import uuid
from django.db import models


class Project(models.Model):
    """
    Represents a project with metadata including name, status, date range,
    and geolocation address. Each project has a unique UUID and validated location.
    """

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True,
        help_text="Automatically generated unique identifier for the project."
    )
    name = models.CharField(
        max_length=255, unique=True,
        help_text="The name of the project (must be unique)."
    )
    description = models.TextField(
        blank=True, null=True,
        help_text="Optional detailed description of the project."
    )
    start_date = models.DateField(
        help_text="The project's official start date."
    )
    end_date = models.DateField(
        blank=True, null=True,
        help_text="Optional end date of the project."
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        help_text="The current status of the project."
    )
    location = models.CharField(
        max_length=512,
        help_text="Address or location string to be validated via Google Maps API."
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True,
        help_text="Latitude coordinate of the validated location."
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True,
        help_text="Longitude coordinate of the validated location."
    )

    def __str__(self):
        return self.name
