"""
Definition of views.
"""

from .models import Comment # использование модели комментариев
from .forms import CommentForm 
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
# from flask import redirect
from .forms import AnketaForm, BlogForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from .models import Blog

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Домашняя страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина', '2': 'Женщина', '3': 'Нет пола'}
    internet = {'1' : 'Человек', '2': 'Демон', '3':'Ангел', '4':'Нежить', '5':'Эльф', '6':'Дракон'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['gender'] = gender[ form.cleaned_data['gender'] ]
            data['species'] = internet[ form.cleaned_data['species']]
            data['job'] = form.cleaned_data['job']
            data['personality'] = form.cleaned_data['personality']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request):
    """Renders the registration page."""
    
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            
            regform.save()
            
            return redirect('home')
        
    else:
        regform = UserCreationForm()
        
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'regform' : regform,
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.all()  # запрос на выбор всех статей блога из модели

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Блог',
            'posts': posts,  # передача списка статей в шаблон веб-страницы
            'year': datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr)  # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    assert isinstance(request, HttpRequest)
    if request.method == "POST":  # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()  # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(
                id=parametr)  # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save()  # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id)  # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm()  # создание формы для ввода комментария

    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,  # передача конкретной статьи в шаблон веб-страницы
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )


def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные материалы',
            'year':datetime.now().year,
        }
    )

def newpost(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f: Blog = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()

    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',
            'year': datetime.now().year
        }
    )

def videopost(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title': 'Видео-ролики',
            'year': datetime.now().year,
        }
    )