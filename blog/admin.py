from django.contrib import admin

from .models import Post
from .models import Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_on')
    list_filter = ['author', 'created_on']
    search_fields = ['title', 'text', 'author']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)

