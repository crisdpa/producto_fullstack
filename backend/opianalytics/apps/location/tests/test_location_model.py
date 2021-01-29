"""Unit tests for Location model."""
from django.test import TestCase
from django.contrib.gis.geos import Point
from opianalytics.apps.location.models.location import Location
from django.core.exceptions import ValidationError
import pathlib


class LocationModelTestCase(TestCase):
    """Provide the tests of the Location model."""

    def setUp(self):
        self.test_absolue_path = pathlib.Path(__file__).parent.absolute()
    
    def test_int_when_add_valid_coordinates(self):
        # Setup
        latitude = 19.3576284
        longitude = -99.2725381

        # Execution
        location_id = Location.objects.add(latitude, longitude)

        # Validation
        self.assertEqual(type(location_id), int)

    def test_error_when_add_invalid_coordinates(self):
        # Setup
        latitude = '1234'
        longitude = 'abcd'

        # Validation
        self.assertRaises(
            ValidationError,
            lambda: Location.objects.add(latitude, longitude)
        )

    def test_error_when_add_from_csv_not_found(self):
        # Setup
        csv_fake_filename = '{0}/{1}'.format(
            self.test_absolue_path, 'fake.csv'
        )
        
        # Validation
        self.assertRaises(
            ValidationError,
            lambda: Location.objects.add_from_csv(csv_fake_filename)
        )

    def test_3_when_add_from_csv(self):
        # Setup
        csv_filename = '{0}/{1}'.format(
            self.test_absolue_path, 'locations_valid.csv'
        )

        # Execution
        total_locations_added = Location.objects.add_from_csv(csv_filename)
        
        # Validation
        self.assertEqual(total_locations_added, 3)

    def test_2_when_add_from_csv_repeated(self):
        # Setup
        csv_filename = '{0}/{1}'.format(
            self.test_absolue_path, 'locations_repeated.csv'
        )

        # Execution
        total_locations_added = Location.objects.add_from_csv(csv_filename)
        
        # Validation
        self.assertEqual(total_locations_added, 2)
