from django.db import models

# Create your models here.

class logindata(models.Model):
    Email = models.CharField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Cpass = models.CharField(max_length=100,null=True,blank=True)

class cartdata(models.Model):
    User = models.CharField(max_length=30, null=True, blank=True)
    Pname = models.CharField(max_length=100, null=True, blank=True)

    quantity = models.IntegerField(null=True,blank=True)
    total_price = models.IntegerField(null=True,blank=True)
