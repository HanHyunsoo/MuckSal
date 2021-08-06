from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30 , null=True)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank=True)
    writer = models.CharField(max_length=15, default='닉네임을 입력해주세요')

    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

