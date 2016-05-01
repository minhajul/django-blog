from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name