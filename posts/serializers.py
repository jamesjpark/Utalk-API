from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'user', 'title', 'body', 'created_at', 'updated_at',
            'likes', 'dislikes', 'views', 'comments', 'image',
            'blockCount', 'isBlocked'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'post', 'body', 'created_at', 'updated_at',
            'likes', 'dislikes'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')

