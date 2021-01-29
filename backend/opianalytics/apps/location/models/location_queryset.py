from django.db import models
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError
from os import path
import csv


class LocationQuerySet(models.QuerySet):
    """Custom queries for Location."""

    def add(self, latitude: float, longitude: float) -> int:
        """Create a new location."""
        try:
            location = self.create(coordinates=Point(latitude, longitude))
        except Exception:
            raise ValidationError(
                'Latitude and longitude must be a float number'
            )
        return location.pk

    def add_from_csv(self, filename: str) -> int:
        """Create locations from CSV file."""
        locations_added = 0
        if not path.exists(filename):
            raise ValidationError(
                "The file provided doesn't exist"
            )

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                try:
                    latitude = float(row[0])
                    longitude = float(row[1])
                    self.add(latitude, longitude)
                except Exception:
                    pass
                else:
                    locations_added += 1

        return locations_added
