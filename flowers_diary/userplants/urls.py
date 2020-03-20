from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from plants import views

urlpatterns = [
    path('userplants/<int:pk</', views.PlantDetail.as_view())
]
