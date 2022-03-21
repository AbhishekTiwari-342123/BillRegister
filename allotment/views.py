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