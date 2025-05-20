"""
Google Maps Geocoding Module

This module provides functionality to convert addresses into geographic coordinates
(latitude and longitude) using the Google Maps Geocoding API.

The module requires a valid Google Maps API key to be set in the environment
variable GOOGLE_MAPS_API_KEY.

Example:
    >>> coordinates = geocode_address("1600 Amphitheatre Parkway, Mountain View, CA")
    >>> print(coordinates)
    (37.4223878, -122.0841877)
"""

from __future__ import annotations
import os
import requests

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")


def geocode_address(address: str) -> tuple[float, float] | None:
    """
    Convert a physical address to geographic coordinates using Google Maps Geocoding API.

    Args:
        address: The physical address to geocode (e.g.,"1600 Amphitheatre Parkway,Mountain View,CA")

    Returns:
        A tuple containing (latitude, longitude) if successful, or None if no results found

    Raises:
        ValueError: If the API request fails or returns an error status
        requests.exceptions.RequestException: If there's an issue with the HTTP request
        KeyError: If the API response format is unexpected
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": GOOGLE_MAPS_API_KEY}
    response = requests.get(url, params=params, timeout=600)
    data = response.json()

    if data.get("status") == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]

    reason = data.get("error_message") or data.get("status", "Unknown error")
    raise ValueError(f"Google Maps API error: {reason}")
