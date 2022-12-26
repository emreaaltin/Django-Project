from django.forms import ModelForm
from .models import *

class MesajForm(ModelForm):
    class Meta:
        model = Mesaj
        fields = ['isim', 'kullaniciAdi', 'eposta','aciklama']

    def __init__(self, *args, **kwargs):
        super(MesajForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})