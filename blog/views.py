from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.urls import reverse
# Create your views here.


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
