from django.shortcuts import render
from rest_framework.generics import ListAPIView
from blog.models import Post
from blog.models import Contact
from .serializers import PostModelSerializer
from .serializers import ContactModelSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class UserListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
