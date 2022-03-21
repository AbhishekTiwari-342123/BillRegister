
from ast import Str
from email.header import Header
from tkinter import CASCADE
from django.db import models
# Create your models here

########################################################## Scheme Master Table starts ###########################################################


# one-one reln between Major and Sub Major, Total Participation on Sub side, 
# one table for both (Head_No, SubHead_No, Head_Name, SubHead_Name)
class Major_Sub_Head(models.Model):
    Head_Code=models.IntegerField(primary_key=True)
    SubHead_Code=models.IntegerField(unique=True, default=0)
    Head_Name=models.CharField(default="",max_length=250)
    SubHead_Name=models.CharField(default="",max_length=250)

    def __str__(self):
        return str(self.Head_Code)+"-"+str(self.SubHead_Code)

# one-many reln between Major_Sub_Head and Minor_Head, Total Participation on Minor_Head Side
# two tables Major_Sub_Head(Head_Code(key),Head_Name); Minor_Head(MinorHead_Code(key), MinorHead_Name, Head_Code(fkey))
# And Major_Sub_Head(Head_Code(key),Head_Name) already exists in the Major_Sub_Head table
# so only one table Minor_Head(MinorHead_Code(key), MinorHead_Name, Head_Code(fkey)) references Major_Sub_Head table
class Minor_Head(models.Model):
    MinorHead_Code=models.IntegerField(primary_key=True)
    MinorHead_Name=models.CharField(default="",max_length=250)
    Head_Code=models.ForeignKey(Major_Sub_Head, to_field="Head_Code", on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.Head_Code)+"-"+str(self.MinorHead_Code)

# one-many reln between Sub_Major and Schemes, Total Participation on Schemes Side
# two tables Sub_Major(SubHead_No(key),SubHead_Name); Scheme(Scheme_Code(key), Scheme_Name, SubHead_No(fkey))
# And Sub_Major(SubHead_No(key),SubHead_Name) already exists in the Major_Sub_Head table
# so only one table Scheme(Scheme_Code(key), Scheme_Name, SubHead_No(fkey)) references Major_Sub_Head table 
class Scheme(models.Model):
    Scheme_Code=models.IntegerField(primary_key=True)
    Scheme_Name=models.CharField(default="",max_length=250)
    #MinorHead_Code=models.ForeignKey(MinorScheme, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Scheme_Code)

# mapping between Minor Head and Scheme (m:n), unique minor-scheme
class MinorScheme(models.Model):
    MinorHead_Code = models.ForeignKey(Minor_Head, to_field='MinorHead_Code', on_delete=models.CASCADE)
    Scheme_Code = models.ForeignKey(Scheme, to_field='Scheme_Code', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('MinorHead_Code', 'Scheme_Code'),)

    def __str__(self):
        return str(self.MinorHead_Code)+"-"+str(self.Scheme_Code)    

# one-many reln between Scheme and Sub_Scheme, Total Participation on Sub_Scheme Side
# two tables Scheme(Scheme_Code(key),Scheme_Name); Sub_Scheme(SubScheme_Code(key), SubScheme_Name, Scheme_Code(fkey))
# And Scheme(Scheme_Code(key),Scheme_Name) already exists in the Scheme(Scheme_Code(key), Scheme_Name, SubHead_No(fkey)) table
# so only one table Sub_Scheme(SubScheme_Code(key), SubScheme_Name, Scheme_Code(fkey)) references Scheme table
class Sub_Scheme(models.Model):
    SubScheme_Code=models.IntegerField(primary_key=True)
    SubScheme_Name=models.CharField(default="",max_length=250)
    #Scheme_Code=models.ForeignKey(MinorScheme, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.SubScheme_Code)+"-"+str(self.SubScheme_Name)

# mapping between Scheme and Sub Scheme (m:n)
class Scheme_SubScheme(models.Model):
    Scheme_Code = models.ForeignKey(MinorScheme, on_delete=models.CASCADE)
    SubScheme_Code = models.ForeignKey(Sub_Scheme, to_field='SubScheme_Code', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('Scheme_Code', 'SubScheme_Code'),)

    def __str__(self):
        return str(self.Scheme_Code)+"-"+str(self.SubScheme_Code)

# one-many reln between Sub_Scheme and Object_Head, Total Participation on Object_Head Side
# two tables Sub_Scheme(SubScheme_Code(key),SubScheme_Name); Object_Head(Object_Code(key), Object_Name, SubScheme_Code(fkey))
# And Sub_Scheme(SubScheme_Code(key),SubScheme_Name) already exists in the Sub_Scheme(SubScheme_Code(key), SubScheme_Name, Scheme_Code(fkey)) table
# so only one table Object_Head(Object_Code(key), Object_Name, SubScheme_Code(fkey)) references Sub_Scheme table
class Object_Head(models.Model):
    Object_Code=models.IntegerField(default=0)
    Object_Name=models.CharField(default="",max_length=250)
    SubScheme_Code=models.ForeignKey(Scheme_SubScheme, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('Object_Code', 'SubScheme_Code'),)

    def __str__(self):
        return str(self.SubScheme_Code)+" - "+str(self.Object_Code)+" - "+str(self.Object_Name)

########################################################## Scheme Master Table ends ###########################################################


########################################################## Active Tables starts ###########################################################

# Allotment to various Object Heads under Salary Register (136, 156, 403, 523)
class Salary_Allotment(models.Model):
    Object_Code=models.ForeignKey(Object_Head, on_delete=models.CASCADE)
    Allotment_Amount=models.IntegerField(default=0)

    def __str__(self):
        return str(self.Object_Code)

# table for recording bills under Salary Register (active register)
# this register is accessed after filter ( pay, hra, da, etc) from the view as per input given by the user on the form
# this is register for salary, and the filters will be fetched from the 'salary allotment'
class Salary_Register(models.Model):
    Bill_Type=models.ForeignKey(Salary_Allotment, on_delete=models.CASCADE)
    Bill_Number=models.CharField(primary_key=True, max_length=20)
    Description=models.TextField(max_length=300, default="")
    Bill_Date=models.DateField(auto_now=False)
    Bill_Amount=models.IntegerField(default=0)
    Bill_Expenditure=models.IntegerField(default=0)
    Bill_Balance=models.IntegerField(default=0)
    Bill_Remark=models.CharField(default="",max_length=250)

