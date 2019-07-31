from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .models import Portfolio
from django.utils import timezone

def home(request):

    return render(request, 'home.html')

def create(request):

    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    blogs = Blog.objects.all()
    
    return render(request, 'home.html', {'blogs' : blogs})

def record(request):

    blogs = Blog.objects.all()

    return render(request, 'record.html', {'blogs' : blogs})

def portfolio(request):
    portfolios=Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})