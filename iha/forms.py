from django import forms
from .models import Kira

class RentalForm(forms.ModelForm):
    class Meta:
        model = Kira
        fields = ['baslangıc_tarih', 'baslangıc_saat', 'bitiş_tarih', 'bitiş_saat', 'Adet', 'iha']
