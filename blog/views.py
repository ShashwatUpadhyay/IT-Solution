from django.shortcuts import render
from . import models

# Create your views here.


def blogs(request):
    l = models.Blog.objects.all().latest('created_at')
    blogs = models.Blog.objects.exclude(uid=l.uid).order_by('-created_at')
    return render(request, 'blogs.html',{'latest': l, 'blogs': blogs})

def blog(request, slug):
    blog = models.Blog.objects.get(slug=slug)
    more = models.Blog.objects.exclude(slug=slug).order_by('-created_at')[:3]
    return render(request, 'blog.html',{'blog': blog, 'more': more})
