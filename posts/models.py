from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from users.models import User
from django.db.models import F
from rest_framework import generics, status


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    

class LikePostAPIView(generics.GenericAPIView):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user

        # Check if the user has already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            # User has already liked, return a message or handle accordingly
            return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new like
        like = Like.objects.create(user=user, post=post)

        # Increment the likes count on the post using F() expression
        Post.objects.filter(id=post_id).update(likes=F('likes') + 1)

        return Response({"post_id": post_id, "likes_count": post.likes}, status=status.HTTP_200_OK)
