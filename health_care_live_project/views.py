from django.http import HttpResponse
from service.models import Department
from service.models import DoctorDetail
from service.models import AppointmentDetail
from django.shortcuts import render
def homePage(request):
    return render(request,'index.html')

def aboutPage(request):
    return render(request,'about.html')

def servicePage(request):
    # print("call")
    department_details=Department.objects.all()
    # print(department_details)
    # print(department_details.query)
    return render(request,'service.html',{'department_details':department_details})

def department_view(request):
    # Your view logic here
    return render(request, 'department.html')

def doctor_view(request):
    # Your view logic here
    return render(request, 'doctor.html')

def contactPage(request):
    return render(request,'contact.html')

def allDoctorPage(request,id):
#    print(id)
   all_doctor=DoctorDetail.objects.filter(department_name_id=id)
#    print(all_doctor)
   return render(request,'doctor.html',{'all_doctor':all_doctor})

def singleDoctorDetails(request,id):
    single_doctor=DoctorDetail.objects.get(id=id)
    # print(single_doctor)
    return render(request,'department_details.html',{'single_doctor':single_doctor}) 
def appointmentPage(request):
    # Your view logic here
    return render(request, 'appointment.html')

def appointmentPage(request,id):
    my_list=[]
    msg=''
    Doctore_detail=DoctorDetail.objects.filter(id=id).values()
    # print(Doctore_detail)
    # print(Doctore_detail[0]['doctor_full_name'])
    dict1={}
    dict1['doc_name']=Doctore_detail[0]['doctor_full_name']
    
    doc_department_id=Doctore_detail[0]['department_name_id']
    Deparment_details=Department.objects.filter(id=doc_department_id).values()
    # print(Deparment_details)
    dict1['department_name']=Deparment_details[0]['department_name']
    
    # print(dict1)
    my_list.append(dict1)
    print(my_list)
    # my_list=[doc_name,department_name]

    
    if request.method=="POST":
        a_department_name=request.POST['a_department_name']
        a_doctor_name=request.POST['a_doctor_name']
        a_date=request.POST['a_date']
        a_time=request.POST['a_time']
        full_name=request.POST['full_name']
        phone=request.POST['phone']
        message=request.POST['message']
        # print(a_department_name,a_doctor_name,a_date,a_time,full_name,phone,message)
        app_data=AppointmentDetail(app_department_name=a_department_name,app_doctorr_name=a_doctor_name,app_date=a_date,app_time=a_time,full_name=full_name,mobile_num=phone,message=message)
        app_data.save()
       

    return render(request,'appointment.html',{'my_list':my_list})

