from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import *

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to = 'images/',null=True)
    
class cart(models.Model):
    name = models.CharField(max_length=255, blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to = 'cart/',null=True)
    id_data = models.CharField(blank=True, null=True,max_length=532)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 


class orders(models.Model):
    name = models.CharField(max_length=500,null=True)
    address = models.CharField(max_length=20000,null=True)
    quantity = models.CharField(max_length=2000,null=True)
    item = models.CharField(max_length=1000, null=True)
    city = models.CharField(null=True, max_length=250)
    phone = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=1000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    zip = models.CharField(max_length=250, null=True)
    price = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to = 'images/',null=True)


class guestuser(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=10000, null=True, blank=True)


class OTP(models.Model):
    key = models.CharField(max_length=6)
    ip = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 


class confirmed(models.Model):
    confirmation = models.CharField(max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)      

class email_taken(models.Model):
    email_field = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 


class get_email(models.Model):
    e_field = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 

class premaccount(models.Model):
    name = models.CharField(max_length=1000)
    ip = models.CharField(max_length=10000)


class prevaccount(models.Model):
    pre = models.CharField(max_length=10000,null=True,blank=True)
    new = models.CharField(max_length=10000,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 



class eOTP(models.Model):
    key = models.CharField(max_length=6)
    ip = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 


class econfirmed(models.Model):
    confirmation = models.CharField(max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=10000, null=True)      

class eemail_taken(models.Model):
    email_field = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 


class eget_email(models.Model):
    e_field = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 


class myaddres(models.Model):
    address = models.CharField(max_length=100000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    city = models.CharField(max_length=250, null=True)
    zip = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=10000, null=True)
    last = models.CharField(max_length=10000, null=True)

class selected(models.Model):
    address = models.CharField(max_length=100000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    city = models.CharField(max_length=250, null=True)
    zip = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=10000, null=True)
    last = models.CharField(max_length=10000, null=True)