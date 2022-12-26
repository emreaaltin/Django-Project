from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if kullanici != '' and email != '' and sifre1 != '' and sifre2 != '' :
            if sifre1 == sifre2:
                if User.objects.filter(username=kullanici).exists():
                    messages.error(request, 'Bu kullanıcı adı zaten mevcut!')
                    return redirect('giris2')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Bu e-Posta adresi zaten mevcut!')
                    return redirect('giris2')
                elif len(sifre1) < 6:
                    messages.error(
                        request, 'Şifre en az 6 karakter olmalıdır!')
                    return redirect('giris2')
                elif kullanici.lower() in sifre1.lower():
                    messages.error(
                        request, 'Kullanıcı adı ve şifre benzer olmamalıdır!')
                    return redirect('giris2')
                else:
                    user = User.objects.create_user(
                        username=kullanici, email=email, password=sifre1)
                    user.save()
                    messages.success(request, 'Kullanıcı oluşturuldu!')
                    return redirect('index')
            else:
                messages.error(request, 'Şifreler Uymuyor')
                return redirect('giris2')
        else:
            messages.error(request, 'Tüm Alanların Doldurulması Zorunludur')
            return redirect('giris2')
    return render(request, 'giris2.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']
        user = authenticate(request, username = kullanici , password = sifre)
        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı!')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı Adı Veya Şifre Hatalı')
            return redirect('giris')


    return render(request, 'giris.html')
def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı!')
    return redirect('index')
