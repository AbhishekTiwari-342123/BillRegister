
from django.db import models
# Create your models here


class Alloted_Total(models.Model):
    Salary_Total_Allotment=models.IntegerField(default=0)


class Allotment_Salary(models.Model):
    Bill_Number=models.CharField(primary_key=True, max_length=20)
    Description=models.TextField(max_length=300, default="")
    Bill_Amount=models.IntegerField(default=0)
    Bill_Expenditure=models.IntegerField(default=0)
    Bill_Balance=models.IntegerField(default=0)
