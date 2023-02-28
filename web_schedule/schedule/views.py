from django.shortcuts import render

from .forms import *


menu = ['Главная', 'Расписание', 'О нас']
schdl = ['День недели', 'Предмет', 'Аудитория', 'Преподаватель', 'Тип Занятий', 'Время']
data_tb = Schedule.decode()
data_tb = Schedule.sort_schedule(data_tb)
context = {'title': 'Расписание', 'menu': menu, 'schedule': schdl, 'data_tb': data_tb}


def index(request):
    return render(request, 'schdle/schedule.html', context=context)


def enter_page(request):
    enter_form = EnterForm()
    context = {'form': enter_form, 'menu': menu, 'title': 'Вход в аккаунт'}
    return render(request, 'schdle/enter_user.html', context=context)


def reg_page(request):
    reg_form = RegForm()
    context = {'form': reg_form, 'menu': menu, 'title': 'Регистрация'}
    return render(request, 'schdle/register_page.html', context=context)

