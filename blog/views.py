from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs=Blog.objects #쿼리셋 #메소드
    return render(request, 'home.html', {'blogs': blogs})

    #쿼리셋과 메소드의 형식
    #모델.쿼리셋(objects).메소드

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력 내용 데이터베이스에 넣어줌
    blog= Blog()
    blog.title= request.GET['title']
    blog.body= request.GET['body']
    blog.pub_date= timezone.datetime.now()
    blog.save() #데이터베이스에 저장해라
    return redirect('/blog/'+str(blog.id))