from django import forms
from django.core.exceptions import ValidationError

from .models import *


class MainForm(forms.Form):
    data_teachers = forms.FileField(label='Данные об учетелях')
    data_lessons = forms.FileField(label='Данные об уроках')
    data_auds = forms.FileField(label='Данные об аудиториях')
    data_groups = forms.FileField(label='Данные об группах учащихся')
    working_week = forms.IntegerField(label='Рабочая неделя')
    max_lessons = forms.IntegerField(label='Максимальное кол-во предметов в день')
    min_break_between_lessons = forms.IntegerField(label='Минимальный перерыв между уроками')
    max_break_between_lessons = forms.IntegerField(label='Максимальный перерыв между уроками')
    after_lesson_max_break = forms.IntegerField(label='После какого максимальный перерыв')