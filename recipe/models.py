from django.db import models
from django.conf import settings
from django.db.models.fields import related

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    ingredient = models.TextField(null=True)
    hits = models.PositiveIntegerField(default=0)
    # food = models.OneToOneField("diet.Food", on_delete=models.CASCADE)


    def __srt__(self):
        return self.title

    @property
    def click(self):
        self.hits += 1
        self.save()