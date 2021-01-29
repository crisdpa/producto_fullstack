from django.urls import path, re_path
from .v1.location import location

urlpatterns = [
    path(
        r'v1/location',
        location.Location.as_view(),
        name='api-v1-location'
    ),
]
