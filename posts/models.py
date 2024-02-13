from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from users.models import User


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    comments = models.ManyToManyField('Comment', blank=True, related_name='post_comments')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    blockCount = models.IntegerField(default=0)
    isBlocked = models.BooleanField(default=False)

    def __str__(self):
        return self.title
   
class Comment(models.Model):
    user = models.ManyToManyField(User, null=True)
    post = models.ManyToManyField(Post, null=True, related_name='post_comments')
    body = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.body



