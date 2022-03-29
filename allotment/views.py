from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import *

# Create your views here.

def login_user(request):
    if request.method == "POST":

        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username, password=password)
        if user:
            print(user)
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("<h1>Incorrect Credentials , User was not recognised. New User ?  Register <a href='register' }'>here</a>")            
    else:                      
        return render(request,'salary/login.html')


def home(request):
    return HttpResponse('Home')


def salaryRegister(request):
    if request.method=="POST":
        print(request.POST)
        new_entry=Salary_Register(Bill_Type=Salary_Allotment.objects.get(id=request.POST.get('bill_type')),
        Bill_Number=request.POST.get('bill_no'),
        Description=request.POST.get('bill_description'),
        Bill_Date=request.POST.get('bill_date'),
        Bill_Amount=request.POST.get('bill_amount'),
        Bill_Remark=request.POST.get('bill_remark'),
        Bill_Expenditure=request.POST.get('bill_amount'),
        Bill_Balance=25550000-int(request.POST.get('bill_amount')))  
        new_entry.save()
        return redirect('salary-register')
    else:
        types=Salary_Allotment.objects.all()
        entries=Salary_Register.objects.all()
        for x in types:
            print(x.id)
        return render(request,'salary/salaryRegisterForm.html',{'types':types,'entries':entries})        

def adminHome(request):
    return render(request,'admin/adminBase.html')

  