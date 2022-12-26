from django.db import models
from django.utils.text import slugify
class Kategori(models.Model):
    isim = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.isim

class AltKategori(models.Model):
    isim = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.isim


# Create your models here.
class Urun(models.Model):
    Kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE , null=True)
    sub_category = models.ManyToManyField(AltKategori)
    isim = models.CharField(max_length=50)
    aciklama=models.TextField(max_length=150)
    fiyat = models.IntegerField()
    fotograf = models.FileField(upload_to='urunler/', null=True, blank = True)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.isim
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)













