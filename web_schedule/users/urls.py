from django.urls import path

from .views import *


urlpatterns = [
    path('login/', AuthPage.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('reg/', RegPage.as_view(), name='reg'),
    path('profile/', CreateProfilePageView.as_view(), name='profile'),

]
