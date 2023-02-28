from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('enter_user/', enter_page, name='auth'),
    path('reg_new_user/', reg_page, name='reg')
]
