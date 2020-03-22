from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plant
        fields=['id','common_name','science_name','temp_min','temp_max','shade_tollerance','precipitation_min','precipitation_max','ph_min','ph_max','growth_period','toxicity']