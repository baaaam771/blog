from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
# Create your views here.

def home(request):
    blogs=Blog.objects #쿼리셋 #메소드
    #블로그 모든 글들을 대상으로
    blog_list =Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자른다
    paginator= Paginator(blog_list, 3)
    #request 받은 페이지가 뭔지 알아낸다(페이지 번호)(request페이지를 변수에 담는다)
    page= request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts= paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

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