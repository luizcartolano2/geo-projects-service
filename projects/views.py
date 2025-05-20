"""
Project ViewSet Module

This module defines the ViewSet for the Project model which provides
default CRUD operations (Create, Retrieve, Update, Delete) through
Django REST Framework's ModelViewSet.

The ViewSet handles all HTTP methods (GET, POST, PUT, PATCH, DELETE)
and integrates with the ProjectSerializer for data validation and conversion.
"""

from rest_framework import viewsets
from .models import Project
from .serializer import ProjectSerializer


# pylint: disable=too-many-ancestors
class ProjectViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Project instances.

    Inherits from ModelViewSet which provides the following actions by default:
    - list (GET /api/projects/)
    - create (POST /api/projects/)
    - retrieve (GET /api/projects/{id}/)
    - update (PUT /api/projects/{id}/)
    - partial_update (PATCH /api/projects/{id}/)
    - destroy (DELETE /api/projects/{id}/)

    Attributes:
        queryset (QuerySet): The queryset that should be used for returning
                            objects from this view. Defaults to all Projects.
        serializer_class (Serializer): The serializer class that should be used
                                      for validating and deserializing input,
                                      and for serializing output.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
