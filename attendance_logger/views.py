from django.shortcuts import render,redirect
from .models import AttendanceRecord
import datetime
from collections import defaultdict
from .forms import Usercreation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("attendance_logger:home")   

        else:
            return render(request=request,template_name="register.html",context={"error":form.errors})
        
    else:
        form = UserCreationForm()
        context = {
            "form":form,
        }
    return render(request=request,template_name="register.html",context=context)

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            form = login(request,user)
            return redirect("attendance_logger:home")
            
        
    return render(request=request,template_name="login.html")

@login_required
def base(request):
    return render(request=request,template_name="base.html")


@login_required
def home(request):
    today = datetime.date.today()
    lower_range,upper_range = today - datetime.timedelta(days=5),today + datetime.timedelta(days=5)
    date_list = []
    start_date = lower_range
    while start_date <= upper_range:
        date_list.append({"day":start_date.strftime('%A'),"date":start_date.strftime('%d/%m/%Y')})
        start_date += datetime.timedelta(days=1)
    data = AttendanceRecord.objects.filter(date__lte=upper_range,date__gte=lower_range).values()
    names = AttendanceRecord.objects.filter(date__lte=upper_range,date__gte=lower_range).values("employee_name").distinct()
    data_dict = defaultdict(list)
    for record in data:
        data_dict[record['employee_name']].append({"status":record["attendance_status"],"date":record["date"].strftime('%d/%m/%Y')})
    options = [
        {'value':'U','label':'Unmarked'},
        {'value':'P','label':'Present'},
        {'value':'V','label':'Vacation'},
        {'value':'S','label':'Sick'},
        {'value':'L','label':'Late'}
    ]
    print("------------------",data_dict)
    print("------------------",names)
    return  render(request=request,template_name="homepage3.html",context={"data_dict":data_dict, "date_tuple":date_list,"options":options,"names":names})

@login_required
def history(request):
    data = [
        {'x':10,'y':20,'value':5},
        {'x':30,'y':40,'value':10}
    ]
    return render(request=request,template_name="history.html",context={"data":data})

def request_leave(request):
    return render(request=request,template_name="request.html")

