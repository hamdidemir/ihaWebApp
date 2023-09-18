from django import forms
from .models import Kira, iha

class RentalForm(forms.ModelForm):
    class Meta:
        model = Kira
        fields = ['baslangıc_tarih', 'baslangıc_saat', 'bitiş_tarih', 'bitiş_saat', 'Adet', 'iha']

class IhaForm(forms.ModelForm):
    class Meta:
        model = iha
        fields = ['Marka', 'Model', 'Faydalı_yük', 'Havada_kalma_süresi', 'Kanat_açıklığı', 'Maksimum_kalkış_ağırlığı', 'image']


class IhaEditForm(forms.ModelForm):
    class Meta:
        model = iha
        fields = ['Marka', 'Model', 'Faydalı_yük', 'Havada_kalma_süresi', 'Kanat_açıklığı', 'Maksimum_kalkış_ağırlığı', 'image']