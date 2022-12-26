from django.contrib import admin
from .models import *

class bilgi(admin.ModelAdmin):
    list_display = ('isim','aciklama','fiyat')

# Register your models here.
admin.site.register(Urun,bilgi)
admin.site.register(Kategori)
admin.site.register(AltKategori)
