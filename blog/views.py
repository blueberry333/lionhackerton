from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    L= []
    for blog in blogs.all():
        body = blog.body
        L.append(str(body))
    L.split()
    random_result = random.choice(L)
    return render(request, 'blog/home.html', {'L': L, 'random_result': random_result})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    # blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/')