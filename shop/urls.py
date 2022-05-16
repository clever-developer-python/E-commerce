"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import store.views
from django.conf.urls import (
handler400, handler403, handler404, handler500
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', store.views.home, name="home"),
    path('<int:product_id>', store.views.detail, name='detail'),
    path('login/', store.views.login, name='login'),
    path('signup/', store.views.signup, name='signup'),
    path('cart/', store.views.cart, name='cart'),
    path('logout/', store.views.log, name="logout"),
    path('delete-item/<int:id>' , store.views.delete_item ), 
    path('checkout' , store.views.checkout, name="checkout" ),
    path('success/', store.views.done, name='su'),
    path('contact/', store.views.contact, name='contact'),
    path('order/', store.views.order, name='order'),
    path('email/', store.views.email, name='email'),
    path('conf/', store.views.email_sent, name='conf'),
    path('wrong_ip/', store.views.ip_wrong, name='wi'),
    path('wrong_otp/', store.views.email_wrong, name='wo'),
    path('Email_confirmed/', store.views.correct_otp, name='d'),
    path('adminpage/',store.views.adminpage, name='adminpage'),
    path('slogin/', store.views.shiftlogin, name='shiftlogin'),
    path('ssignup/', store.views.shiftsignup, name='shiftsign'),
    path('demail/', store.views.defaultemail, name='de'),
    path('sentemail/',store.views.defemail_sent, name='se')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'store.views.error_page'