from rest_framework import serializers
from .models import Plant

class UserplantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userplant
        fields='__all__'