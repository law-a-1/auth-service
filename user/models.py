from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    role = models.CharField(max_length=255,default='user')

    REQUIRED_FIELDS = []