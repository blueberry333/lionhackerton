from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random
from .models import Blog

# Create your views here.

def create(request):
    blog = Blog()
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/')

def make_blogs():
    blogs = Blog.objects
    return blogs

def show_blogs(request):
    blogs = make_blogs()
    L= []
    for blog in blogs.all():
        body = blog.body
        L.append(body)
    random_result = random.choice(L)
    return render(request, 'blog/home.html', {'random_result': random_result, 'blogs': blogs})

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')
