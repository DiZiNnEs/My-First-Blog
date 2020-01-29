from django.shortcuts import render

from .models import Blog

def index(request):
    blogs = Blog.objects.all().order_by('-pub_date',)
    return render (request, 'index.html', {
        'blogs' : blogs,
        
    })
