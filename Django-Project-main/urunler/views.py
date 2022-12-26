from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    search = ''   
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains = search) |
            Q(Kategori__isim__icontains = search) |
            Q(sub_category__isim__icontains = search) |
            Q(aciklama__icontains = search) 
        ) 
    context = {
        'urunler':urunler,
        'search':search,
        'kategoriler':kategoriler
    }
    return render(request, 'index.html', context)
def sepet(request):
    return render(request, 'sepet.html')
def detail(request,slug):
    urun=Urun.objects.filter(slug = slug)
    context={
        'urun':urun
    }
    return render(request, 'urun.html',context)
def olustur(request):
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ürün Başarıyla Oluşturuldu!')
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'olustur.html', context)

