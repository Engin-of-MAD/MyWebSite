from django.shortcuts import render

from datetime import time
from schedule.models import Schedule
menu = ['Главная', 'Расписание', 'О нас']
schdl = ['День недели', 'Предмет', 'Аудитория', 'Преподаватель', 'Тип Занятий', 'Время']
data_tb = Schedule.decode()
context = {'title': 'Расписание', 'menu': menu, 'schedule': schdl, 'data_tb': data_tb}



def index(request):
    return render(request, 'schdle/schedule.html', context=context)


