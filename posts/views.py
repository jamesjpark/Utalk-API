from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Posted successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        posts = self.get_queryset()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # Customize this method to associate the Comment with the user creating it, if needed.
        serializer.save()

class LikePostAPIView(generics.GenericAPIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user

        # Check if the user has already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            # User has already liked, return a message or handle accordingly
            return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new like
        like = Like.objects.create(user=user, post=post)

        # Increment the likes count on the post
        post.likes += 1
        post.save()

        return Response({"post_id": post_id, "likes_count": post.likes}, status=status.HTTP_200_OK)