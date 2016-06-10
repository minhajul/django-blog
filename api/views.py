from django.shortcuts import render
from rest_framework.generics import ListAPIView
from blog.models import Post
from .serializers import PostModelSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


