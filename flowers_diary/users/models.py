from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    """create and save new user"""
    firebase_uid = models.CharField(max_length=128, null=False, blank=False)
    email = models.CharField(max_length=64, null=False, blank=False, unique=True)
    username = models.CharField(max_length=32, null=True, blank=True, unique=True)
    photo_url = models.CharField(max_length=255, null=True, blank=True)
    email_verified = models.BooleanField(default=False, null=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id', 'firebase_uid', 'USERNAME_FIELD']