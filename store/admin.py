from django import conf
from django.contrib import admin
from .models import Items,cart,orders,guestuser,OTP,confirmed,email_taken,get_email,prevaccount,myaddres

# Register your models here.

admin.site.register(Items)
admin.site.register(cart)
admin.site.register(orders)
admin.site.register(guestuser)
admin.site.register(OTP)
admin.site.register(confirmed)
admin.site.register(email_taken)
admin.site.register(get_email)
admin.site.register(prevaccount)
admin.site.register(myaddres)