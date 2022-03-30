from hashlib import new
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

def adminMajorSub(request):
    if request.method=='POST':
        print(request.POST)
        newentry=Major_Sub_Head(Head_Code=request.POST.get('majorCode'),SubHead_Code=request.POST.get('SubCode'),
        Head_Name=request.POST.get('majorName'),SubHead_Name=request.POST.get('SubName'))
        newentry.save()
        return redirect('majorSub')
    else:
        heads=Major_Sub_Head.objects.all()
        return render(request,'admin/adminMajorSub.html',{'heads':heads})

def adminMinor(request):
    if request.method=='POST':
        print(request.POST)
        newentry=Minor_Head(MinorHead_Code=request.POST.get('minorCode'),
        MinorHead_Name=request.POST.get('minorName'),
        Head_Code=Major_Sub_Head.objects.get(pk=request.POST.get('head')))
        newentry.save()
        return redirect('minor')
    else:
        headCodes=Major_Sub_Head.objects.all()
        print(headCodes[0])
        print(headCodes[0].Head_Code)
        minors=Minor_Head.objects.all()
        return render(request,'admin/adminMinor.html',{'headCodes':headCodes,'minors':minors})

def adminScheme(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'admin/adminScheme.html')

def adminSubScheme(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'admin/adminSubScheme.html')

# Mapping 1 (Scheme to Heads)        
def adminMinor_Scheme(request):
    if request.method=='POST':
        pass
    else:
        heads=Minor_Head.objects.all()
        schemes=Scheme.objects.all()
        return render(request,'admin/adminMap-MinorScheme.html',{'heads':heads,'schemes':schemes})

# Mapping 2 (sub Scheme to Scheme)             
def adminSubScheme_Scheme(request):
    if request.method=='POST':
        pass
    else:
        schemes=Scheme.objects.all()
        subSchemes=Sub_Scheme.objects.all()
        print(subSchemes[2].SubScheme_Name)
        return render(request,'admin/adminMap-Scheme_SubScheme.html',{'subSchemes':subSchemes,'schemes':schemes})

def adminObject(request):
    if request.method=='POST':
        print(request.POST)
        newentry=Object_Head(Object_Code=request.POST.get('objectCode'),Object_Name=request.POST.get('objectName'),
        SubScheme_Code=Scheme_SubScheme.objects.get(id=request.POST.get('scheme')))
        newentry.save()
        return redirect('object')
    else:
        objects=Object_Head.objects.all()
        headSubSchemes=Scheme_SubScheme.objects.all()
        return render(request,'admin/adminObject.html',{'headSubSchemes':headSubSchemes,'objects':objects})



def adminAllotment(request):
    if request.method=='POST':
        print(request.POST)
        newEntry=Salary_Allotment(Object_Code=Object_Head.objects.get(id=request.POST.get('head')),
        Allotment_Amount=request.POST.get('amount'))
        newEntry.save()
        return redirect('allotment')
    else:
        objects=Object_Head.objects.all()
        allotments=Salary_Allotment.objects.all()
        return render(request,'admin/adminAllotment.html',{'objects':objects,'allotments':allotments})
