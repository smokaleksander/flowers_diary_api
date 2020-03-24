from django.shortcuts import render
from rest_framework import status, viewsets,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from plants.serializers import PlantSerializer
from plants.models import Plant
from userplants.models import Userplant
from userplants.serializers import UserplantSerializer
from .pagination import PaginationHandlerMixin
from users.serializers import UserSerializer
# Create your views here.
class Plants(APIView, PaginationHandlerMixin):
    pagination_class=PageNumberPagination

    def get(self,request):
        qs=Plant.objects.all()
        page=self.paginate_queryset(qs)
        if page is not None:
            serializer=self.get_paginated_response(PlantSerializer(page,many=True).data)
        else:   
            serializer=PlantSerializer(plants,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer=PlantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #else    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlantsDetail(APIView):

    def get_object(self, id):
        try:
            return Plant.objects.get(pk=id)
        except Plant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
              
    def get(self,request, id):
        plant=self.get_object(id)
        serializer=PlantSerializer(plant)
        return Response(serializer.data)

    def put(self,request,id):
        plant=self.get_object(id)
        serializer=PlantSerializer(plant,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        plant=self.get_object(id)
        serializer=PlantSerializer(plant,data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPlants(APIView):
    pagination_class=PageNumberPagination

    def get(self,request):
        userplants=UserPlant.objects.all()
        page=PaginationHandlerMixin.paginate_queryset(userplants)
        if page is not None:
            serializer=PaginationHandlerMixin.paginated_response(UserplantSerializer(page,many=True).data)
        else:
            serializer=UserPlantSerializer(userplants,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer=UserPlantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #else    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPlantsDetail(APIView):

    def get_object(self, id):
        try:
            return UserPlant.objects.get(pk=id)
        except UserPlant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
              
    def get(self,request, id):
        userplant=self.get_object(id)
        serializer=UserPlantSerializer(userplant)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        userplant=self.get_object(id)
        serializer=UserPlantSerializer(plant,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        userplant=self.get_object(id)
        serializer=UserPlantSerializer(userplant,data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request,id):
        user=self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)    