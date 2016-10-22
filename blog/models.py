from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name