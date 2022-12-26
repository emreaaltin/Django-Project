
from django.contrib import admin
from django.urls import path
from urunler.views import *
from user.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('sepet/', sepet),
    path('giris/', userRegister, name="register"),
    path('urun/<str:slug>', detail, name='urun'),
    path('olustur/', olustur, name='olustur')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
