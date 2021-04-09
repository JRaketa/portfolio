from django.shortcuts import render

from .models import Blog

def blog(request):
    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs':blogs})
