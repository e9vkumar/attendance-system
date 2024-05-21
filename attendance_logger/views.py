from django.shortcuts import render
from .models import AttendanceRecord
import datetime
# Create your views here.

def register(request):
    return render(request=request,template_name="register.html")

def login(request):
    return render(request=request,template_name="login.html")

def base(request):
    return render(request=request,template_name="base.html")



def home(request):
    today = datetime.date.today()
    lower_range,upper_range = today - datetime.timedelta(days=5),today + datetime.timedelta(days=5)
    date_list = []
    start_date = lower_range
    while start_date <= upper_range:
        date_list.append(start_date.strftime('%d/%m/%Y'))
        start_date += datetime.timedelta(days=1)
    data = AttendanceRecord.objects.all()
    options = [
        {'value':'U','label':'Unmarked'},
        {'value':'P','label':'Present'},
        {'value':'V','label':'Vacation'},
        {'value':'S','label':'Sick'},
        {'value':'L','label':'Late'}
    ]
    return  render(request=request,template_name="homepage3.html",context={"data":data, "date_tuple":date_list,"options":options})


def history(request):
    data = [
        {'x':10,'y':20,'value':5},
        {'x':30,'y':40,'value':10}
    ]
    return render(request=request,template_name="history.html",context={"data":data})

def request_leave(request):
    return render(request=request,template_name="request.html")

