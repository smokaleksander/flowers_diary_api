from django.urls import path

from .views import PlantList, PlantDetail, UserDetail

urlpatterns = [
    path('plants/', PlantList.as_view()),
    path('plants/<int:id>/', PlantDetail.as_view()),
    path('user/', UserDetail.as_view())
]
