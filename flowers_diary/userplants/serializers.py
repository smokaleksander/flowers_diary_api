from rest_framework import serializers
from .models import Plant

class UserplantSerializer(serializers.ModelSerializer):
    class Meta:
        model=['id','Userplant','fields','plant','location','img','info','owner']