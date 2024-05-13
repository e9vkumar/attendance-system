from django.shortcuts import render
from .models import AttendanceRecord
import datetime 
# date,timedelta
# Create your views here.

def register(request):
    return render(request=request,template_name="register.html")

def login(request):
    return render(request=request,template_name="login.html")

def base(request):
    return render(request=request,template_name="base.html")


def home(request):
    employee_names = AttendanceRecord.objects.all().values("employee_name")
    today = datetime.date.today()
    past_dates = [today - datetime.timedelta(days=i) for i in range(5, 0, -1)]
    future_dates = [today + datetime.timedelta(days=i) for i in range(1, 6)]
    print(employee_names)
    attendance_data = {}
    for employee_name in employee_names:
        attendance_data[employee_name] = {}
        for date in past_dates + [today] + future_dates:
            attendance= Attendance.objects.filter(employee_name=employee_name)
            attendance_data[employee_name][date] = attendance.attendance_status

    context = {
        'employees': employee_names,
        'today': today,
        'past_dates': past_dates,
        'future_dates': future_dates,
        'attendance_data': attendance_data
    }
    return render(request, 'homepage.html', context)




def history(request):
    data = [
        {'x':10,'y':20,'value':5},
        {'x':30,'y':40,'value':10}
    ]
    return render(request=request,template_name="history.html",context={"hmdata":data})

def request_leave(request):
    return render(request=request,template_name="request.html")






        #    {% comment %} <option value="Present">Present</option>
        #       <option value="Vacation">Vacation</option>
        #       <option value="Late">Late</option>
        #       <option value="Sick">Sick</option> {% endcomment %}
        #       {% comment %} {% if record.attendance_status == options.value%}
        #       <option value="{{options.value}}">{{options.label}}</option>
        #       {% endif %} {% endcomment %}
        #       {% comment %} {% else %} {% endcomment %}
        #       {% comment %} <option value="">Select an Option</option> {% endcomment %}
        #       {% comment %} {% endif %} {% endcomment %}
        #                     {% comment %} {% for record in attendance_data.employee.employee_id %} {% endcomment %}
        #       {% comment %} {% if record.date == date %}    {% endcomment %}
        #       {% endfor %}