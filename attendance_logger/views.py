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

def filter_record(id,lower_range,upper_range):
    data = AttendanceRecord.objects.filter(employee_id=id,date__lte=upper_range,date__gte=lower_range).values("attendance_status","date")
    return data

def home(request):
    today = datetime.date.today()
    lower_range,upper_range = today - datetime.timedelta(days=5),today + datetime.timedelta(days=5)
    data = AttendanceRecord.objects.all().order_by("employee_id").values("employee_name","employee_id").distinct()
    date_list = []
    start_date = lower_range
    while start_date <= upper_range:
        date_list.append(start_date.strftime('%d/%m/%Y'))
        start_date += datetime.timedelta(days=1)
    # print(date_list)
    data_dict = {}
    for item in data:
        data_dict[item['employee_id']]=filter_record(item['employee_id'],lower_range=lower_range,upper_range=upper_range)
    print(data_dict['01'])

    send_data = {'data':data,'date_tuple':tuple(date_list),'today':today.strftime('%d/%m/%Y'),'lower':lower_range,'upper':upper_range,"attendance_data":data_dict}
    return render(request=request,template_name="homepage.html",context=send_data)

def checkin(request):
    return render(request=request,template_name="checkin.html")

def request_leave(request):
    return render(request=request,template_name="request.html")