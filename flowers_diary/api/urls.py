from django.urls import path, include
from .views import Plants, PlantsDetail, UserPlants, UserPlantsDetail
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('plants/',Plants.as_view()),
    path('plants/<int:id>/', PlantsDetail.as_view())
    path('userplants/',UserPlants.as_view()),
    path('userplants/<int:id>/', UserPlantsDetail.as_view())
]
