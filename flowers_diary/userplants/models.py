from django.db import models
from users.models import User
from plants.models import Plant
# Create your models here.
class Userplant(models.Model):
    nickname=models.CharField(max_length=50, blank=True)
    plant=models.ForeignKey(Plant, on_delete=models.DO_NOTHING)
    location=models.CharField(max_length=80)
    img=models.ImageField(upload_to=None)
    info=models.CharField(max_length=200)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_plants')

    def __str__(self):
        return (self.plant+" "+self.nickname)