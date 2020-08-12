from rest_framework import serializers
from .models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['nickname', 'specie', 'location', 'info','last_watered','last_fertilized','watering_interval','fertilizing_interval', 'owner']
