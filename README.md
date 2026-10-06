# Ex02 Django ORM Web Application
## Date: 06/10/26

## AIM
To develop a Django Application to store and retrieve data from a Student details Database platform using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM

```
admin.py

from django.contrib import admin
from .models import student_DB,student_DBAdmin
admin.site.register(student_DB,student_DBAdmin)

models.py

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
```

## OUTPUT

![alt text](<Screenshot 2026-10-06 220644-1.png>)

## RESULT
Thus the program for creating Student details Database using ORM hass been executed successfully
