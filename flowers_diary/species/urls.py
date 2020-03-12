from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from species import views

urlpatterns = [
    path('species/<int:pk</', views.SpecieDetail.as_view())
]
