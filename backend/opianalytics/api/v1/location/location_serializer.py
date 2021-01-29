from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    coordinates = serializers.ListField(read_only=True)
