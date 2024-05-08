from django.urls import path
from .views import base,register,login,home

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('base/',base,name="base"),
    path('home/',home,name="home"),
]