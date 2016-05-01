from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Post
from .forms import ContactForm


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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit = False)
            contact.save()
            messages.success(request, "Thanks for your feedback!")
            return redirect('blog.views.contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Show login view
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, "You have successfully logged in!")
            return redirect('/')
        else:
            messages.error(request, "Authentication Failed!")
            return render (request, 'login.html', {})
    else:
        return render(request, 'login.html', {})



