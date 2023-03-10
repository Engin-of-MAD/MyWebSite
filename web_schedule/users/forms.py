from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль')
    password1 = forms.CharField(label='Подтверждение пароля')





class ProfileForm(forms.Form):
    login = forms.CharField(label="Логин", max_length=128)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, max_length=128)