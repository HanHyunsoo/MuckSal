from django.db import models
from django.conf import settings

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __srt__(self):
        return self.title