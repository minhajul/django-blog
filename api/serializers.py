from rest_framework import serializers

from blog.models import Post


class PostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'text',
        ]
        