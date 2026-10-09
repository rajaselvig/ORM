# Ex02 Django ORM Web Application
## Date: 09/10/26

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
from.models import Vechicle_dB,Vechicle_dBAdmin
admin.site.register(Vechicle_dB,Vechicle_dBAdmin)

models.py

from django.db import models
from django.contrib import admin
class Vechicle_dB(models.Model):
     license_no=models.CharField(max_length=15,primary_key=True)
     faults_found=models.TextField()
     owner_name=models.CharField(max_length=30)
     owner_contact=models.IntegerField()
     owner_address=models.TextField()
     deposit_payed=models.FloatField()
     total_amount=models.FloatField()
class Vechicle_dBAdmin(admin.ModelAdmin):
    list_display=["license_no","faults_found","owner_name","owner_contact","owner_address","deposit_payed","total_amount"]
```

## OUTPUT

![alt text](<Screenshot 2026-10-09 231835.png>)

## RESULT
Thus the program for creating Student details Database using ORM hass been executed successfully
