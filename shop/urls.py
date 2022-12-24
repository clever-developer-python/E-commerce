
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
    path('', store.views.home, name="home"), #fix
    path('<int:product_id>', store.views.detail, name='detail'), #fix
    path('login/', store.views.login, name='login'),#fix
    path('signup/', store.views.signup, name='signup'),#fix
    path('cart/', store.views.checkout, name='cart'),#fix
    path('logout/', store.views.log, name="logout"),
    path('delete-item/<int:id>' , store.views.delete_item, name="delete" ), 
    path('checkout' , store.views.checkout, name="checkout" ), #fix
    path('success/', store.views.done, name='su'),
    path('order/', store.views.order, name='order'),#fix
    path('conf/', store.views.email_sent, name='conf'),#fix
    path('wrong_ip/', store.views.ip_wrong, name='wi'),#fix
    path('wrong_otp/', store.views.email_wrong, name='wo'),#fix
    path('Email_confirmed/', store.views.correct_otp, name='d'),#fix
    path('slogin/', store.views.shiftlogin, name='shiftlogin'),
    path('ssignup/', store.views.shiftsignup, name='shiftsign'),
    path('myadd/', store.views.myaddress, name='aee'),
    path('aa/',store.views.myaddressform, name='add'),
    path('aa2/',store.views.myaddressform2, name='add2'),
    path('sa/',store.views.selectadd, name='selected'),
    path('r/<int:product_id>',store.views.addr,name="ad"),
    path('r/uq',store.views.uq,name="uq"),
     path('contact/',store.views.uq,name="contact"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'store.views.error_page'
