from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

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
        return render(request,'Register/login.html')


def home(request):
    return HttpResponse('Home')


def salaryRegister(request):
    if request.method=="POST":
        bill_type=request.POST.get('bill_type')
        bill_no=request.POST.get('bill_no')
        bill_description=request.POST.get('descp')
        bill_date=request.POST.get('bill_date')
        bill_amount=request.POST.get('bill_amount')
        bill_remark=request.POST.get('remark')
        
    else:
        return HttpResponse('render the form')        