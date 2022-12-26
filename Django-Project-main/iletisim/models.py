from django.db import models

# Create your models here.

class Mesaj(models.Model):
    isim = models.CharField(max_length=20)
    kullaniciAdi = models.CharField(max_length=15)
    eposta = models.EmailField()
    aciklama = models.CharField(max_length=300)

    def __str__(self):
        return self.eposta