from django.db import models
from species.models import Specie
from users.models import User
# Create your models here.
class Plant(models.Model):
    nickname=models.CharField(max_length=50, blank=True)
    specie=models.ForeignKey(Specie, on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    img=models.ImageField(upload_to=None)
    others=models.CharField(max_length=100)
    Owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_plants')

class Watering(models.Model):
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    plant=models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='waterings')