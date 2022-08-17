from __future__ import unicode_literals
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Sum,F
from django.contrib.auth import authenticate, login as loginuser,logout
from django.http import Http404
import json
import random
import string
from .models import Items,cart as ca,orders,guestuser,OTP,confirmed,email_taken,get_email,prevaccount,eget_email,eemail_taken,econfirmed,eOTP,myaddres as address,selected
from django.core.mail import send_mail
import re
from mailjet_rest import Client

#main backed of website project started on 31 jan 2022
#home page backend code!

api_key = '92cdd8cf0247854404d38fd5e335b452'
api_secret = '682905addd62eabb7a24de2f2934b6a6'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

def home(request):

        if request.user.is_authenticated:
            if guestuser.objects.filter(name = request.user):
                username = 'guest'
                items = Items.objects.all()
                return render(request, 'index.html',{'items':items,'guest':username})

            else:

                if address.objects.filter(user = request.user).exists():
                    pass

                else:
                    return redirect('add2')
                items = Items.objects.all()
                return render(request, 'index.html',{'items':items})

        else:
            if User.is_anonymous:
             alert = 'This Account is auto generated please note down the username the password is the same as the username or create an account!'
             items = Items.objects.all()
             S = 10 
             ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
             user = User.objects.create_user(username = str(ran), password=str(ran))
             final = authenticate(username=user,password=user)
             if user is not None:
                loginuser(request, final)
                g = guestuser()
                g.name = request.user
                g.save()
                return render(request, 'index.html',{'items':items, 'alert':alert})       
            return render(request, 'index.html')

        

#product detail page backend code!
def detail(request, product_id):
    product = get_object_or_404(Items, pk=product_id)
    if request.method == "POST":

            print(product.name)

            if ca.objects.filter(name = product.name, user=request.user).exists():
                return redirect('cart')

            else:

                c = ca()
                c.name = product.name
                c.image = product.image
                c.user = request.user
                c.quantity = request.POST.get('quantity')
                c.price = product.price
                c.save()
            
            return redirect('cart')
    return render(request, 'detail.html',{'product':product})


#cart code
def cart(request):
    #checking if cart is empty
    if ca.objects.filter(user = request.user).count() > 0:
        items = ca.objects.filter(user = request.user)
        #calculations
        total_price = ca.objects.filter(user = request.user).aggregate(total=Sum(F('price') * F('quantity')))['total']
        print(total_price)
        if request.method == 'POST':    
                return redirect('checkout')
            
    
        return render(request, 'cart.html',{'items':items,'total':total_price,'user':request.user})
    
    else:
        return render(request, 'none.html')


def signup(request):
    
    if request.method == 'POST':
        # User has info and wants an account now!

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, request.POST.get('username')):
                    pass
        else:
                return render(request, 'signup.html',{'error':'Email isnt valid'})
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.get(username=request.POST.get('username'))
                return render(request, 'signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'))
                
                auth.login(request,user)

                code1 = random.randint(1,9)
                code2 = random.randint(1,9)
                code4 = random.randint(1,9)
                code3 = random.randint(1,9)
                code5 = random.randint(1,9)
                code = f"{code1}{code2}{code3}{code4}{code5}"
                o = OTP()
                o.key = code
                o.ip = request.META.get('REMOTE_ADDR')
                o.user = request.user
                o.save()

                usr = request.POST.get('username')
                
                data = {
                  'Messages': [
                    {
                      "From": {
                        "Email": "isanamessenger@gmail.com",
                        "Name": "Isana no reply"
                      },
                      "To": [
                        {
                          "Email": f"{usr}",
                          "Name": "Customer"
                        }
                      ],
                      "Subject": "Otp Code",
                      "TextPart": f"Your OTP is: {code} Thank you for using our products!  sincerly, Ninaad Lead Developer Of Isana If anyone else got this message i apoligze i am building a website and i must have sent this to the wrong email!" ,
                      "CustomID": "AppGettingStartedTest"
                    }
                  ]
                }
                result = mailjet.send.create(data=data)

                g = get_email()
                g.e_field = f'{usr}'
                g.user = request.user
                g.save()
                return redirect('conf')
        else:
            return render(request, 'signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')

#login
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            print(request.user)
            auth.login(request, user)
            print(request.user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')



    
    
def log(request):
    logout(request)
    return redirect('login')
#delete items in cart!

def delete_item(request , id ):
    print(id)
    ca.objects.get(pk = id).delete()
    return redirect('cart')


def email_sent(request):
    print(request.META['REMOTE_ADDR'])
    if request.method == 'POST':
        get_key = request.POST.get('key')
        if OTP.objects.filter(key = get_key).exists():
            print('okay')

        else:
            print('security warning')
            return redirect('wo')
        if OTP.objects.filter(ip = request.META['REMOTE_ADDR']).exists():
            print('okay')
            c = confirmed()
            c.confirmation = 'yes'
            c.user = request.user
            c.save()

            e = email_taken()
            for gu in get_email.objects.filter(user = request.user):
                e.email_field = gu.e_field
                e.user = request.user
                e.save()
                return redirect('home')

            


            return redirect('d')

        else:
            print('security warning')
            return redirect('wi')
    return render(request, 'conf.html')


def email_wrong(request):
    if request.method == 'POST':
        get_key = request.POST.get('key')
        if OTP.objects.filter(key = get_key).exists():
            print('okay')

        else:
            print('security warning')
            return redirect('wo')
        if OTP.objects.filter(ip = request.META['REMOTE_ADDR']).exists():
            print('okay')
            c = confirmed()
            c.confirmation = 'yes'
            c.user = request.user
            c.save()

            e = email_taken()
            for gu in get_email.objects.filter(user = request.user):
                e.email_field = gu.e_field
                e.user = request.user
                e.save()

            


            return redirect('d')

        else:
            print('security warning')
            return redirect('wi')
    return render(request, 'wrong.html')


def correct_otp(request):
    return render(request, 'doneotp.html')


def ip_wrong(request):
    if request.method == 'POST':
        get_key = request.POST.get('key')
        if OTP.objects.filter(key = get_key).exists():
            print('okay')

        else:
            print('security warning')
            return redirect('wo')
        if OTP.objects.filter(ip = request.META['REMOTE_ADDR']).exists():
            print('okay')
            c = confirmed()
            c.confirmation = 'yes'
            c.user = request.user
            c.save()

            e = email_taken()
            for gu in get_email.objects.filter(user = request.user):
                e.email_field = gu.e_field
                e.user = request.user
                e.save()
            return redirect('d')

        else:
            print('security warning')
            return redirect('wi')
    return render(request, 'ipwrong.html')


def checkout(request):

    if guestuser.objects.filter(name = request.user).exists():
        return redirect('shiftlogin')

    if selected.objects.filter(user = request.user).count() > 0:
        pass

    else:
        if address.objects.filter(user = request.user).count() > 0:
            return redirect('selected')

        else:
            return redirect('add')


    if confirmed.objects.filter(user = request.user).exists():
            pass

    else:
        return redirect('conf')


    if ca.objects.filter(user = request.user).count() > 0:
        if confirmed.objects.filter(user = request.user).exists() or econfirmed.objects.filter(user = request.user).exists():
            total_price = ca.objects.filter(user = request.user).aggregate(total=Sum(F('price') * F('quantity')))['total']
            dataemail = eget_email.objects.filter(user = request.user)
            datadd = selected.objects.filter(user = request.user)
            cadata = ca.objects.filter(user = request.user)

            if request.method == 'POST':
                for c in ca.objects.filter(user = request.user):
                    body = json.loads(request.body)
                    data = body['address']
                    o = orders()
                    o.address = data
                    o.name = body['firstname']
                    o.item = c.name
                    o.quantity = c.quantity
                    o.city = body['state']
                    if email_taken.objects.filter(user = request.user).exists():
                        for em in email_taken.objects.filter(user = request.user):                 
                            o.email = em.email_field

                    else:
                            for eg in eget_email.objects.filter(user = request.user):
                                o.email = eg.e_field
                    o.zip = body['zipcode']
                    o.price = total_price
                    o.image = c.image
                    o.user = request.user
                    o.save()

                    for a in selected.objects.filter(user = request.user):
                        a.delete()               
                    for c in ca.objects.filter(user = request.user):
                        c.delete()



            
            return render(request, 'checkout.html', {'total_price':total_price,'dataemail':dataemail,'datadd':datadd,'cadata':cadata})
            

        else:
           return redirect('email')


    else:
        return render(request, 'none.html')



def done(request):
       name = orders.objects.filter(user = request.user)
       return render(request, 'success.html', {'name':name})

def contact(request):
    return render(request, 'contact.html')


def error_page(request,exception ):
    return render(request, '404.html')
    
    
def order(request):
    if orders.objects.filter(user = request.user).count() > 0:
        o = orders.objects.filter(user = request.user)
        return render(request, 'order.html',{'orders':o})
    
    else:
        return render(request, 'none2.html')


def adminpage(request):
    if request.user.is_superuser:
        var = orders.objects
        return render(request, 'admincustom.html',{'items':var})

    else:
        raise Http404



def shiftlogin(request):
    if request.user.is_authenticated:
            pass

    else:
        return redirect('login')
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            c = prevaccount()
            c.pre = request.user
            c.new = request.POST.get('username')
            c.user = request.user
            c.save()
            p = prevaccount()
            old = prevaccount.objects.filter(pre = request.user)

            print(request.POST.get('username'))
            print(request.user)
            auth.login(request, user)
            for cartitem in ca.objects.filter(user = c.pre):
                    add = ca()
                    add.name = cartitem.name
                    add.price = cartitem.price
                    add.quantity = cartitem.quantity
                    add.image = cartitem.image
                    add.user = request.user
                    add.save()

            print(request.user)



            return redirect('home')
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')



def shiftsignup(request):
    if request.user.is_authenticated:
        pass

    else:
        return redirect('signup')
    if request.method == 'POST':
        # User has info and wants an account now!
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, request.POST.get('username')):
                    pass
        else:
                return render(request, 'signup.html',{'error':'Email isnt valid'})
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.get(username=request.POST.get('username'))
                return render(request, 'signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'))
                if user is not None:
                    c = prevaccount()
                    c.pre = request.user
                    c.new = request.POST.get('username')
                    c.user = request.user
                    c.save()
                    p = prevaccount()
                    old = prevaccount.objects.filter(pre = request.user)

                    print(request.POST.get('username'))
                    print(request.user)
                    auth.login(request, user)

                    code1 = random.randint(1,9)
                    code2 = random.randint(1,9)
                    code4 = random.randint(1,9)
                    code3 = random.randint(1,9)
                    code5 = random.randint(1,9)
                    code = f"{code1}{code2}{code3}{code4}{code5}"
                   
                    get_data_email = 'ninaadr26@gmail.com'
                    o = OTP()
                    o.key = code
                    o.ip = request.META.get('REMOTE_ADDR')
                    o.user = request.user
                    o.save()
                    usr = request.POST.get('username')
                
                    data = {
                      'Messages': [
                        {
                          "From": {
                            "Email": "isanamessenger@gmail.com",
                            "Name": "Isana no reply"
                          },
                          "To": [
                            {
                              "Email": f"{usr}",
                              "Name": "Customer"
                            }
                          ],
                          "Subject": "Otp Code",
                          "TextPart": f"Your OTP is: {code} Thank you for using our products!  sincerly, Ninaad Lead Developer Of Isana If anyone else got this message i apoligze i am building a website and i must have sent this to the wrong email!" ,
                          "CustomID": "AppGettingStartedTest"
                        }
                      ]
                    }
                    result = mailjet.send.create(data=data)
                    g = get_email()
                    g.e_field = f'{usr}'
                    g.user = request.user
                    g.save()



                    for cartitem in ca.objects.filter(user = c.pre):
                            add = ca()
                            add.name = cartitem.name
                            add.price = cartitem.price
                            add.quantity = cartitem.quantity
                            add.image = cartitem.image
                            add.user = request.user
                            add.save()
                            return redirect('conf')
        else:
            return render(request, 'signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')



def myaddress(request):
    if guestuser.objects.filter(name = request.user).exists():
        return redirect('home')
    get_address = address.objects.filter(user = request.user)
    return render(request, 'address.html', {'g':get_address})


def myaddressform(request):
    if guestuser.objects.filter(name = request.user).exists():
        return redirect('ae')
    if request.method == 'POST':
        a = address()
        a.address = request.POST.get('address')
        a.city = request.POST.get('city')
        a.last = request.POST.get('last')
        a.name = request.POST.get('first')
        a.user = request.user
        a.zip = request.POST.get('zip')
        a.save()
    return render(request, 'addad.html')



def selectadd(request):
    if guestuser.objects.filter(name = request.user).exists():
        return redirect('home')
    get_address = address.objects.filter(user = request.user)

    for s in selected.objects.filter(user = request.user):
                s.delete()

    if request.method == 'POST':

        get_item = request.POST.get('data')

        if get_item == 'select an address':
            return render(request, 'select.html', {'g':get_address,'error':'Please choose a proper address!'})

        s = selected()
        for a in address.objects.filter(user = request.user, address=get_item):
            s.user = request.user
            s.address = a.address
            s.city = a.city
            s.zip = a.zip
            s.name = a.name
            s.last = a.last

        s.save()
        return redirect('checkout')
    
    return render(request, 'select.html', {'g':get_address})


def myaddressform2(request):
    if address.objects.filter(user = request.user).count() > 0:
        return redirect('home')
    if guestuser.objects.filter(name = request.user).exists():
        return redirect('home')
    if request.method == 'POST':
        a = address()
        a.address = request.POST.get('address')
        a.city = request.POST.get('city')
        a.last = request.POST.get('last')
        a.name = request.POST.get('first')
        a.user = request.user
        a.zip = request.POST.get('zip')
        a.save()
        return redirect('home')
    return render(request, 'addad.html')

    