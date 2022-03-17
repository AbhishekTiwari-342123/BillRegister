
from django.contrib import admin
from .models import *
# Register your models here.



class MajorSubHead_Admin(admin.ModelAdmin):
    list_display=('Head_Code','SubHead_Code','Head_Name','SubHead_Name')

class MinorHead_Admin(admin.ModelAdmin):
    list_display=('MinorHead_Code','MinorHead_Name','Head_Code')

class Scheme_Admin(admin.ModelAdmin):
    list_display=('Scheme_Code','Scheme_Name','MinorHead_Code')

class SubScheme_Admin(admin.ModelAdmin):
    list_display=('SubScheme_Code','SubScheme_Name','Scheme_Code')

class ObjectHead_Admin(admin.ModelAdmin):
    list_display=('Object_Code','Object_Name','SubScheme_Code')

class SalaryAllotment_Admin(admin.ModelAdmin):
    list_display=('Object_Code','Allotment_Amount')

class SalaryRegister_Admin(admin.ModelAdmin):
    list_display=('Bill_Type','Bill_Number','Bill_Date','Description','Bill_Amount','Bill_Expenditure','Bill_Balance','Bill_Remark')


class MinorScheme_Admin(models.Model):
    list_display=('MinorHead_Code','Scheme_Code')

admin.site.register(Major_Sub_Head,MajorSubHead_Admin)
admin.site.register(Minor_Head,MinorHead_Admin)
admin.site.register(Scheme,Scheme_Admin)
admin.site.register(Sub_Scheme,SubScheme_Admin)
admin.site.register(Object_Head,ObjectHead_Admin)
admin.site.register(Salary_Allotment,SalaryAllotment_Admin)
admin.site.register(MinorScheme,MinorScheme_Admin)
admin.site.register(Salary_Register,SalaryRegister_Admin)

