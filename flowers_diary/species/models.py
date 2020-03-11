from django.db import models

# Create your models here.
class Specie(models.Model):
    common_name=models.CharField( max_length=50)
    science_name=models.CharField( max_length=50)
    temp_min=models.FloatField()
    temp_max=models.FloatField()
    shade_tollerance=models.CharField( max_length=50)
    precipitation_min=models.FloatField()
    precipitation_max=models.FloatField()
    ph_min=models.FloatField()
    ph_max=models.FloatField()
    growth_period=models.CharField( max_length=50)
    toxicity=models.CharField( max_length=50)