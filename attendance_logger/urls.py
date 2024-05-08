from django.urls import path
from .views import base,register,login,home,checkin,request_leave

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('base/',base,name="base"),
    path('home/',home,name="home"),
    path('checkin/',checkin,name="checkin"),
    path("request/",request_leave,name="request"),
]