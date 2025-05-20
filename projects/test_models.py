"""
Test Module for Project Model

This module contains unit tests for the Project model in the projects application.
It verifies the model's behavior including creation, validation, and constraints.
"""
import uuid
from django.test import TestCase
from django.utils import timezone
from projects.models import Project


class ProjectModelTest(TestCase):
    """
    Test case class for the Project model.

    This class contains test methods to verify:
    - Project creation with valid data
    - Model constraints and validations
    - Field requirements and defaults
    - Uniqueness constraints
    """

    def setUp(self):
        """
        Set up test data for each test method.

        Creates a sample Project instance with:
        - Name: "Test Project"
        - Random UUID
        - Current date as start_date
        - Status: "pending"
        - Sample Google headquarters address as location
        """
        self.project = Project.objects.create(
            name="Test Project",
            uuid=uuid.uuid4(),
            start_date=timezone.now().date(),
            status="pending",
            location="1600 Amphitheatre Parkway, Mountain View, CA"
        )

    def test_project_creation(self):
        """
        Test project creation with valid data.

        Verifies:
        - Project is created with correct name
        - Status is set correctly
        - UUID is generated and not None
        - end_date is None by default
        - Only one project exists in database
        """
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(self.project.status, "pending")
        self.assertIsNotNone(self.project.uuid)
        self.assertIsNone(self.project.end_date)
        self.assertEqual(Project.objects.count(), 1)

    def test_project_unique_name(self):
        """
        Test project name uniqueness constraint.

        Verifies that attempting to create a project with a duplicate name
        raises an exception, ensuring the name field uniqueness constraint.
        """
        with self.assertRaises(Exception):
            Project.objects.create(
                name="Test Project",  # duplicate name
                uuid=uuid.uuid4(),
                start_date=timezone.now().date(),
                status="in progress",
                location="Another Location"
            )
