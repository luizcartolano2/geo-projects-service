"""
Django REST Framework serializers for the Project model.

This module defines serializers that handle the conversion between Project model instances
and JSON/other content types, and vice versa. It includes geocoding functionality that
automatically converts addresses to geographic coordinates using Google Maps API.
"""

from rest_framework import serializers

from .google_maps import geocode_address
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model with geocoding capabilities.

    This serializer handles serialization and deserialization of Project instances,
    including all fields defined in the Project model. It automatically geocodes
    location addresses to latitude/longitude coordinates during creation and updates.

    The serializer provides:
    - Automatic field generation based on the Project model
    - Address geocoding via Google Maps API
    - Validation of location addresses
    - Complete CRUD operation support

    Attributes:
        Meta (class): Inner class containing metadata for the serializer.
    """

    class Meta:
        """
        Metadata options for the ProjectSerializer.

        Attributes:
            model (Model): The Django model that this serializer is based on.
            fields (str or tuple): Specifies which fields should be included in the serialization.
                                  '__all__' indicates that all model fields should be included.
        """
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new Project instance with geocoded coordinates.

        Args:
            validated_data (dict): Validated data for project creation

        Returns:
            Project: The newly created Project instance

        Raises:
            serializers.ValidationError: If geocoding fails for the provided address
        """
        validated_data = self._add_coordinates(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing Project instance with optional geocoding.

        Args:
            instance (Project): The project instance to update
            validated_data (dict): Validated data for project update

        Returns:
            Project: The updated Project instance

        Raises:
            serializers.ValidationError: If geocoding fails for the provided address
        """
        if "location" in validated_data:
            validated_data = self._add_coordinates(validated_data)
        return super().update(instance, validated_data)

    @staticmethod
    def _add_coordinates(validated_data):
        """
        Internal method to add latitude/longitude coordinates to validated data.

        Args:
            validated_data (dict): The validated data dictionary

        Returns:
            dict: The validated data with added latitude and longitude

        Raises:
            serializers.ValidationError: If the address cannot be geocoded
        """
        location = validated_data.get("location")
        try:
            lat, lng = geocode_address(location)
        except ValueError as e:
            raise serializers.ValidationError({"location": str(e)})
        validated_data["latitude"] = lat
        validated_data["longitude"] = lng
        return validated_data
