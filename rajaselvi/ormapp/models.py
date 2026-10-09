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