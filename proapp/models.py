from django.db import models

# Create your models here

class categorydata(models.Model):
    Cname = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="profile",null=True,blank=True)

class productdata(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Pname = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Pdescription = models.CharField(max_length=100, null=True, blank=True)
    Pimage = models.ImageField(upload_to="profile", null=True, blank=True)

class invoicedata(models.Model):
    Uname = models.CharField(max_length=100, null=True, blank=True)
    Emailid = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=300, null=True, blank=True)
    Phone = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
class contactdata(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Emailid = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=300, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)








