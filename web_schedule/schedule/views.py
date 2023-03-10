from django.views.generic import FormView

from users.utils import DataMixin
from .forms import *


class MainPage(DataMixin, FormView):
    template_name = 'schdle/main_page.html'
    form_class = MainForm
    success_url = 'schdle/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


