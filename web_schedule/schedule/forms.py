from django import forms

from .models import *


class SignUP(forms.Form):
    btn_enter = None
    btn_reg = None


class EnterForm(forms.Form):
    login = forms.CharField(label="Логин", max_length=128)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, max_length=128)


class RegForm(forms.Form):
    email = forms.CharField(label="Email", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Имя", max_length=32)
    last_name = forms.CharField(label="Фамилия", max_length=32)
    # type_org = forms.ModelChoiceField(label="Тип организации", queryset=TypesOrgs.objects.all())
    nickname = forms.CharField(label="Никнейм", max_length=64)
    avatar = forms.FileField(label="Аватарка")