"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from app.models import Blog


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label = 'Имя персонажа', min_length=2, max_length=50)
    city = forms.CharField(label='Где он родился', min_length=2, max_length=50)
    gender = forms.ChoiceField(label='Пол', choices=[('1','Мужской'),('2','Женский'),('3','Нет пола')],
                             widget = forms.RadioSelect, initial=1)
    species = forms.ChoiceField(label = 'Раса',
                                 choices = (('1', 'Человек'),
                                 ('2', 'Демон'),
                                 ('3', 'Ангел' ),
                                 ('4', 'Нежить'),
                                 ('5', 'Эльф'),
                                 ('6', 'Дракон')), initial=1)
    job = forms.CharField(label='Чем он занимается', min_length=2, max_length=50)
    personality = forms.CharField(label='Характер', min_length=1)
    message = forms.CharField(label='Коротко о нём', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # используемая модель
        fields = ('text',)  # требуется заполнить только поле text
        labels = {'text': "Комментарий"}  # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинки"}
