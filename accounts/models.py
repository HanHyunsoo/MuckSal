from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    password=models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    is_premium = models.BooleanField(default=False)
    register_dttm = models.DateField(auto_now=True, verbose_name="가입날짜")
    def __str__(self): #데이터가 문자열 변환될 때 어떻게 나오는 지 보려고
        return self.username

    class Meta:
        db_table = 'user_table'
        verbose_name = 'user'