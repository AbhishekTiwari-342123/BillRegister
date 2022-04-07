from django.urls import path
from . import views

urlpatterns= [

    # login 
    #path('',views.login_user, name='login'),

    # home after login
    path('home/', views.home, name='home'),
    path('home/salary-register/', views.salaryRegister, name='salary-register'),
    path('admin1/home/', views.adminHome, name="admin-home"),
    
    # 1st dropdown under Major
    path('admin1/home/majorSub/', views.adminMajorSub, name="majorSub"),
    
    # 2nd dropdown under Major
    path('admin1/home/minor/', views.adminMinor, name="minor"),

    # 1st dropdown under Scheme
    path('admin1/home/scheme/', views.adminScheme, name="scheme"),

    # 2nd dropdown under Scheme
    path('admin1/home/subScheme/', views.adminSubScheme, name="subScheme"),

    # 1st dropdown under Mapping
    path('admin1/home/minor-scheme/', views.adminMinor_Scheme, name="minor-scheme"),
    
    # 2nd dropdown under Mapping
    path('admin1/home/scheme-subScheme/', views.adminSubScheme_Scheme, name="scheme-subScheme"),
    

    path('admin1/home/object/', views.adminObject, name="object"),

    path('admin1/home/allotment/', views.adminAllotment, name="allotment"),

    path('admin1/home/addUser/', views.addUser, name="addUser"),
    

    path('', views.login_user, name='login')

]