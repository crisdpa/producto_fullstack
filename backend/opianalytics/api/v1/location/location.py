from rest_framework.views import APIView
from opianalytics.apps.location.models import Location as LocationModel
from .location_serializer import LocationSerializer
from rest_framework.response import Response


class Location(APIView):
    queryset = LocationModel.objects.none()

    def get(self, request, format=None):
        locations = LocationModel.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response({
            'rows': serializer.data
        })
