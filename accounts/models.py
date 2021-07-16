from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    is_premium = models.BooleanField(default=False)