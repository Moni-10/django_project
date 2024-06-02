from django.db import models

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=150)
    department_description=models.TextField()

    def __str__(self):
        return self.department_name

class DoctorDetail(models.Model):
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    doctor_full_name=models.CharField(max_length=150)
    gender=models.CharField(max_length=10)
    age=models.SmallIntegerField()
    education_status=models.CharField(max_length=150)
    work_experience=models.SmallIntegerField()
    email_id=models.CharField(max_length=100)
    mobile_number=models.BigIntegerField()
    doctor_description=models.TextField()
    avialiable_work_hours=models.SmallIntegerField()
    state=models.CharField(max_length=100) 
    city=models.CharField(max_length=100)

class AppointmentDetail(models.Model):
    app_department_name=models.CharField(max_length=100)
    app_doctorr_name=models.CharField(max_length=100)
    app_date=models.DateField()
    app_time=models.CharField(max_length=50)
    full_name=models.CharField(max_length=100)
    mobile_num=models.BigIntegerField()
    message=models.TextField()
    


