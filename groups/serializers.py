from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, unique=True)
    scientific_name = serializers.CharField (max_length=50, unique=True)