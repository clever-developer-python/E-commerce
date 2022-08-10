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
    path('cart/', store.views.checkout, name='cart'),
    path('logout/', store.views.log, name="logout"),
    path('delete-item/<int:id>' , store.views.delete_item, name="delete" ), 
    path('checkout' , store.views.checkout, name="checkout" ),
    path('success/', store.views.done, name='su'),
    path('contact/', store.views.contact, name='contact'),
    path('order/', store.views.order, name='order'),
    path('conf/', store.views.email_sent, name='conf'),
    path('wrong_ip/', store.views.ip_wrong, name='wi'),
    path('wrong_otp/', store.views.email_wrong, name='wo'),
    path('Email_confirmed/', store.views.correct_otp, name='d'),
    path('adminpage/',store.views.adminpage, name='adminpage'),
    path('slogin/', store.views.shiftlogin, name='shiftlogin'),
    path('ssignup/', store.views.shiftsignup, name='shiftsign'),
    path('myadd/', store.views.myaddress, name='aee'),
    path('aa/',store.views.myaddressform, name='add'),
    path('sa/',store.views.selectadd, name='selected')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'store.views.error_page'