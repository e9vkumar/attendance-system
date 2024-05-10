from django.urls import path
from .views import base,register,login,home,history,request_leave

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('base/',base,name="base"),
    path('home/',home,name="home"),
    path('history/',history,name="history"),
    path("request/",request_leave,name="request"),
]