from django.db import models
from django.conf import settings
from accounts.models import *

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30 , null=True)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank=True)
    writer = models.CharField(max_length=15, default='닉네임을 입력해주세요')
    created_at = models.DateTimeField('date published')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, related_name = 'like')
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

