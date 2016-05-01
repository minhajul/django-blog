from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
def details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'details.html', {'post': post})