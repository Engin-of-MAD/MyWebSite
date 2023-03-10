from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, FormView
from django.http import Http404

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect, get_object_or_404

from .forms import *
from .utils import DataMixin
from schedule.models import AuthUser

class AuthPage(DataMixin, LoginView):
    template_name = 'usr/login.html'
    form_class = AuthenticationForm
    success_url = 'home'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


class RegPage(DataMixin, CreateView):
    template_name = 'usr/reg_page.html'
    form_class = UserCreationForm
    success_url = 'home'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        print(self.request.user)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class CreateProfilePageView(CreateView):
    template_name = 'usr/user_profile.html'
    fields = ['profile_pic', 'bio', 'tg']

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        return queryset.get(slug=slug)

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    success_url = reverse_lazy('tasks')


class ShowProfilePageView(DetailView):
    template_name = 'usr/user_profile.html'
    slug_field = 'custom_slug_field'


def logout_user(request):
    logout(request)
    return redirect('login')


