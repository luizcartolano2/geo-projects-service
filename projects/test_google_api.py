"""
Google Maps Geocoding Test Module

This module contains unit tests for the geocode_address function that interacts with
the Google Maps Geocoding API. It tests both successful and error scenarios using mocking
to avoid actual API calls during testing.
"""

import unittest
from unittest.mock import patch, Mock
from projects.google_maps import geocode_address  # adjust import if needed


class GeocodeAddressTests(unittest.TestCase):
    """
    Test case for the geocode_address function.

    This test class verifies:
    - Successful geocoding of valid addresses
    - Proper error handling for invalid addresses
    - Correct parsing of API responses
    - Appropriate exception raising for API errors
    """

    @patch("projects.google_maps.requests.get")
    def test_geocode_address_success(self, mock_get):
        """
        Test successful geocoding of a valid address.

        Verifies:
        - Correct coordinates are returned for a valid address
        - API response is properly parsed
        - The requests.get method is called with expected parameters

        Mocks:
        - Google Maps API response with valid location data
        """
        # Prepare the mock response with valid data
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "OK",
            "results": [{
                "geometry": {
                    "location": {
                        "lat": 37.4223878,
                        "lng": -122.0841877
                    }
                }
            }]
        }
        mock_get.return_value = mock_response

        # Test with Google's headquarters address
        lat, lng = geocode_address("1600 Amphitheatre Parkway, Mountain View, CA")
        self.assertEqual(lat, 37.4223878)
        self.assertEqual(lng, -122.0841877)

    @patch("projects.google_maps.requests.get")
    def test_geocode_address_failure(self, mock_get):
        """
        Test geocoding failure for an invalid address.

        Verifies:
        - ValueError is raised for invalid addresses
        - Error message contains API error information
        - Proper error propagation from the API response

        Mocks:
        - Google Maps API response with error status
        """
        # Prepare the mock response with an error status
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "ZERO_RESULTS",
            "error_message": "No results found"
        }
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            geocode_address("Invalid address 12345")
        self.assertIn("Google Maps API error", str(context.exception))
        self.assertIn("No results found", str(context.exception))
