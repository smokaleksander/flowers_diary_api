from django.db import models

from users.models import User


# Create your models here.
class Plant(models.Model):
    nickname = models.CharField(max_length=50, blank=True)
    specie = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=150)
    #img = models.ImageField(upload_to='plant_photos')
    info = models.CharField(max_length=200)
    last_watered = models.DateField()
    last_fertilized = models.DateField()
    watering_interval = models.IntegerField()
    fertilizing_interval = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_plants')

    def __str__(self):
        return (self.specie + " " + self.nickname)
