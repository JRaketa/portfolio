from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog

def blog(request):
    blogs_list = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blogs_list, 1)

    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request, 'blog.html', {'blogs':blogs})
