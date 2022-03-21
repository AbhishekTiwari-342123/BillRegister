from django.urls import path
from . import views

urlpatterns= [

    # login 
    path('',views.login_user, name='login'),

    # home after login
    path('home/', views.home, name='home'),
]