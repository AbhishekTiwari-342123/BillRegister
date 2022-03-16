
from email.header import Header
from tkinter import CASCADE
from django.db import models
# Create your models here

class Major_Head(models.Model):
    Head_No=models.IntegerField(primary_key=True)
    Head_Name=models.CharField(default="",max_length=250)

class Sub_Major(models.Model):
    Head_No=models.ForeignKey(Major_Head, on_delete=CASCADE)
    Sub_Head_No=models.ForeignKey()
    Sub_Head_Name=models.CharField(default="")


class Alloted_Salary_Total(models.Model):
    pass

class Allotment_Salary(models.Model):
    Bill_Number=models.CharField(primary_key=True, max_length=20)
    Description=models.TextField(max_length=300, default="")
    Bill_Amount=models.IntegerField(default=0)
    Bill_Expenditure=models.IntegerField(default=0)
    Bill_Balance=models.IntegerField(default=0)
