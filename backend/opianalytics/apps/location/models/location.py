"""Location model definition."""
from django.db import models
from django.contrib.gis.db.models import PointField
from .location_queryset import LocationQuerySet

class Location(models.Model):
    """
    Location class
    """
    objects = LocationQuerySet.as_manager()

    coordinates = PointField(
        geography=True,
        unique=True,
    )


    class Meta:
        """Global settings."""

        indexes = [
            models.Index(
                fields=['coordinates']
            )
        ]

    def __str__(self):
        """Return a human readable information."""
        return str(self.coordinates)

    def clean(self):
        """Make custom validations or modify attributes."""
        super().clean()

    def save(self, *args, **kwargs):
        """Save or update."""
        self.full_clean()
        super().save(*args, **kwargs)