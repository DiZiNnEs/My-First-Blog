from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Blog

def index(request):
    blogs = Blog.objects.all().order_by('-pub_date')
    return render (request, 'index.html', {
        'blogs' : blogs,
    })

def post_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render (request, 'post_detail.html', {
        'blog' : blog,
    })
    