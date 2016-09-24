from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import ContactForm
from django.views import generic


# Create home view with 3 latest blog.
def home(request):
    blogs = Post.objects.all().order_by('-id')[:6]
    return render(request, 'home.html', {'blogs': blogs})


# Show Blog page with pagination
class BlogView(generic.ListView):
    model = Post
    template_name = 'blogs.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page', self.paginate_by)


# Show blog details view
class BlogDetailsView(generic.DetailView):
    model = Post
    template_name = 'details.html'
    context_object_name = 'blog'


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

