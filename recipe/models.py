from django.db import models
from django.conf import settings

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # food = models.OneToOneField("diet.Food", on_delete=models.CASCADE)


    def __srt__(self):
        return self.title