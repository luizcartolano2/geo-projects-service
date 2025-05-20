"""
URL Configuration for Projects API

This module defines the URL routing for the Projects API endpoints using
Django REST Framework's DefaultRouter. It automatically generates URL patterns
for standard CRUD operations on Project resources.

The router creates the following endpoints by default:
- /projects/ - List and create projects (GET, POST)
- /projects/{id}/ - Retrieve, update, or delete specific project (GET, PUT, PATCH, DELETE)
"""
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet

# Create a router and register our ViewSet with it
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

# Schema view setup
schema_view = get_schema_view(
    openapi.Info(
        title="Projects API",
        default_version='v1',
        description="API documentation for the Projects app",
        contact=openapi.Contact(email="support@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

# The URL patterns are now determined automatically by the router
urlpatterns = [
    # Include all router URLs
    *router.urls,
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
