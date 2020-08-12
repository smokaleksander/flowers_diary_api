from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import PaginationHandlerMixin
from plants.models import Plant
from plants.serializers import PlantSerializer
from users.models import User
from users.serializers import UserSerializer


class PlantList(APIView, PaginationHandlerMixin):
    """
    List all plants
    """
    pagination_class = PageNumberPagination

    def get(self, request):
        qs = Plant.objects.all()
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_paginated_response(PlantSerializer(page, many=True).data)
        else:
            serializer = PlantSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantDetail(APIView):
    """
    Plant detail view
    """

    def get_object(self, id):
        try:
            return Plant.objects.get(pk=id)
        except Plant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        plant = self.get_object(id)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    def put(self, request, id):
        plant = self.get_object(id)
        serializer = PlantSerializer(plant, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        plant = self.get_object(id)
        serializer = PlantSerializer(plant, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    user detail endpoint
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
