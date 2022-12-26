from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages

# Create your views here.

def mesaj(request):
    form = MesajForm()
    if request.method == 'POST':
        form = MesajForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Mesaj Başarıyla Gönderildi!')
            return redirect('index')
        else:
            messages.error(request,'Lütfen tüm alanları doldurduğunuzdan emin olun!')
            return redirect('mesaj')
    context = {
        'form':form
    }
    return render(request, 'form.html', context)