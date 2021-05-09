from django import forms

from .models import Comment
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'com_text',)


class UserRegForm(UserCreationForm):
    username=forms.CharField(label="Имя пользователя",widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1=forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label="Подверждение пароля",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label="E-mail",widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields=('username','email','password1','password2')
        
class UserLogForm(AuthenticationForm):
    username=forms.CharField(label="Имя пользователя",widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
