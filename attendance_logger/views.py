from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request=request,template_name="register.html")

def login(request):
    return render(request=request,template_name="login.html")

def base(request):
    return render(request=request,template_name="base.html")

def home(request):
    return render(request=request,template_name="homepage.html")

def checkin(request):
    return render(request=request,template_name="checkin.html")

def request_leave(request):
    return render(request=request,template_name="request.html")