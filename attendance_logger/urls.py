from django.urls import path
from .views import base,register,Login,home,history,request_leave

app_name = "attendance_logger"

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',Login,name="login"),
    path('base/',base,name="base"),
    path('home/',home,name="home"),
    path('history/',history,name="history"),
    path("request/",request_leave,name="request"),
]