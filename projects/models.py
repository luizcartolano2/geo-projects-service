"""
Project Model Module

Defines the core Project model for the projects application, representing
work initiatives with associated metadata, status tracking, and geolocation data.
"""
import uuid
from django.db import models


class Project(models.Model):
    """
    A model representing a work project with comprehensive tracking capabilities.

    Projects are characterized by:
    - Unique identifier and name
    - Temporal attributes (start/end dates)
    - Status lifecycle tracking
    - Geolocation data with address validation
    - Descriptive metadata

    The model automatically generates a UUID and provides geocoding integration
    through the location field which populates latitude/longitude coordinates.
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
        """
        String representation of the Project instance.

        Returns:
            str: The project name for display purposes.
        """
        return self.name
