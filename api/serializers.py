from rest_framework import serializers
from blog.models import Post
from blog.models import Contact


class PostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'text'
        ]


class ContactModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        field = [
            'id',
            'name',
            'email',
            'message'
        ]
