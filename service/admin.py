from django.contrib import admin
from service.models import Department
from service.models import DoctorDetail
from service.models import AppointmentDetail

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display=("department_name","department_description")


class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display=("department_name","doctor_full_name","gender","age","education_status","work_experience","email_id","mobile_number","doctor_description","avialiable_work_hours","state","city")

class AppointmentDetailsAdmin(admin.ModelAdmin):
    list_display=("app_department_name","app_doctorr_name","app_date","app_time","full_name","mobile_num","message")


admin.site.register(Department,DepartmentAdmin)   
admin.site.register(DoctorDetail,DoctorDetailsAdmin)
admin.site.register(AppointmentDetail,AppointmentDetailsAdmin)