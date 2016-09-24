from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from blog.models import Post
from blog.models import Contact
from django.contrib.auth.models import User
from .serializers import PostModelSerializer
from .serializers import ContactModelSerializer
from .serializers import UserModelSerializer


class PostListView (generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class ContactListView (generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer


class UserListView (generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAdminUser,)

