from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import random
from .models import Blog
from .form import BlogPost

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
    imageminus=''
    image0 =''
    image1 =''
    image2 =''
    image3 =''
    image4 =''
    for blog in blogs.all():
        body = blog.body
        L.append(body)

    if L == []:
        L = ['empty']

    random_result = random.choice(L)


    if len(L) >= 25 :
        imageminus = 'imageminus'
    elif len(L) >= 20 :
        image0 = 'image0'
    elif len(L) >= 10:
        image1 = 'image1'
    elif len(L) >= 5:
        image2 = 'image2'
    elif len(L) > 0 and L != ['empty']:
        image3 = 'image3'
    elif L == ['empty']:
        image4 = 'image4'

    return render(request, 'blog/home.html', {'random_result': random_result, 'blogs': blogs, 'imageminus':imageminus, 'image0':image0, 'image1':image1, 'image2':image2, 'image3':image3, 'image4':image4})


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = BlogPost(request.POST)
        if form.is_valid():
            # {'name': '수정된 이름', 'image': <InMemoryUploadedFile: Birman_43.jpg 	(image/jpeg)>, 'gender': 'female', 'body': '수정된 내용'}
            blog.body = form.cleaned_data['body']
            blog.save()
            return redirect('/')

    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = BlogPost()
        return render(request, 'blog/edit_post.html',{'form':form})

