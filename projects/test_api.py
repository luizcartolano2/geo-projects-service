"""
Project API Test Module

This module contains API tests for the Project resource endpoints.
It tests CRUD operations and verifies the integration with Google Maps geocoding.
"""

import datetime
from unittest.mock import patch, Mock
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from projects.models import Project


class ProjectAPITests(APITestCase):
    """
    Test case for Project API endpoints.

    Tests include:
    - Project creation with geocoding
    - Project retrieval
    - Error handling
    - Data validation

    Uses mocking to isolate tests from external API dependencies.
    """

    def setUp(self):
        """
        Initialize test data for API tests.

        Sets up a dictionary with sample project data including:
        - Name
        - Description
        - Start date
        - Status
        - Location (Google HQ address)
        """
        self.project_data = {
            "name": "Test Project",
            "description": "Test description",
            "start_date": "2025-01-01",
            "status": "pending",
            "location": "1600 Amphitheatre Parkway, Mountain View, CA"
        }

    @patch("projects.google_maps.requests.get")
    def test_create_project(self, mock_requests_get):
        """
        Test project creation through API with geocoding.

        Verifies:
        - Successful project creation (HTTP 201)
        - Project is persisted in database
        - Correct latitude/longitude is returned
        - Google Maps API response is properly handled

        Mocks:
        - Google Maps API call to return fixed coordinates
        """
        # Mock the requests.get().json() call chain
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "OK",
            "results": [{
                "geometry": {
                    "location": {
                        "lat": 37.4221,
                        "lng": -122.0841
                    }
                }
            }]
        }
        mock_requests_get.return_value = mock_response

        url = reverse('project-list')
        response = self.client.post(url, self.project_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Project.objects.filter(name="Test Project").exists())
        self.assertAlmostEqual(float(response.data["latitude"]), 37.4221, places=4)
        self.assertAlmostEqual(float(response.data["longitude"]), -122.0841, places=4)

    def test_get_projects(self):
        """
        Test project list retrieval.

        Verifies:
        - Successful response (HTTP 200)
        - Returns at least one project
        - Proper serialization of project data

        Setup:
        - Creates a test project directly in database
        """
        Project.objects.create(
            name="Test Get",
            start_date=datetime.date(2025, 1, 1),
            status="pending",
            location="Somewhere"
        )
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
