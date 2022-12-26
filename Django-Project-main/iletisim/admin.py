from django.contrib import admin
from .models import Mesaj

class MesajBaslik(admin.ModelAdmin):
    list_display = ('eposta','isim','kullaniciAdi')

# Register your models here.

admin.site.register(Mesaj, MesajBaslik)