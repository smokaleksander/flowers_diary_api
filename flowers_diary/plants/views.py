from django.shortcuts import render
from rest_framework import generics
from .models import Plant
from .serializers import PlantSerializer
# Create your views here.
class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Plant.objects.all()
    serializer_class=PlantSerializer