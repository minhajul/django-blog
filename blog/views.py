from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create home view with 3 latest blog.
def home(request):
    blogs = Post.objects.all().order_by('-id')[:6]
    return render(request, 'home.html', {'blogs': blogs})

# Show blog view with all blog
def blogs(request):
    blogs = Post.objects.all().order_by('-id')
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blogs.html', {'blogs': blogs})

# Show blog details view
def details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'details.html', {'post': post})

# Show contact view
def contact(request):
    return render(request, 'contact.html')
