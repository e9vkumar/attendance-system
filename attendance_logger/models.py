from django.db import models

# Create your models here.

def get_choices():
    choices = {("U","Unmarked"),("P","Present"),("V","Vacation"),("L","Late"),("S","Sick")}
    return choices

class AttendanceRecord(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10)
    date = models.DateField()
    attendance_status = models.CharField(max_length=1,choices=get_choices(),default="P")

    def __str__(self):
        return self.employee_name
    
    def get_status_for_date(self):
        data = AttendanceRecord.objects.get(employee_id=self.employee_id,date=self.date).attendance_status
        return data
