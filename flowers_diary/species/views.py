from django.shortcuts import render
from rest_framework import generics
from .models import Specie
from .serializers import PlantSerializer
# Create your views here.
class SpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Specie.objects.all()
    serializer_class=SpecieSerializer