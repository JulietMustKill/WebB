"""
Definition of urls for Web1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include
from django.contrib import admin
from app import forms, views
admin.autodiscover()


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('anketa/', views.anketa, name='anketa'),
    path('blog', views.blog, name='blog'),
    path('newpost', views.newpost, name='newpost'),
    path('videopost', views.videopost, name='videopost'),
    path(r'^(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path('links/', views.links, name='links'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),  
    path('user/registration/', views.registration, name='registration'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
