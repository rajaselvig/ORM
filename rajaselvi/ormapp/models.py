from django.db import models
from django.contrib import admin
class student_DB(models.Model):
    Ref_No=models.IntegerField()
    Name=models.CharField(max_length=10)
    Dob=models.DateField()
    Email=models.EmailField()
    Percent=models.FloatField()
    Address=models.TextField()
    Hobbies=models.CharField(max_length=20)
class student_DBAdmin(admin.ModelAdmin):
    list_display=["Ref_No","Name","Dob"]