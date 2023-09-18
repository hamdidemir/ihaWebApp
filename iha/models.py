from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class iha(models.Model):
    Marka = models.CharField(max_length=64)
    Model = models.CharField(max_length=64)
    Faydalı_yük = models.IntegerField(default=0)
    Havada_kalma_süresi = models.IntegerField(default=0)
    Kanat_açıklığı = models.IntegerField(default=0)
    Maksimum_kalkış_ağırlığı = models.IntegerField(default=0)
    image = models.ImageField(upload_to='iha_images/', blank=True, null=True)

    def __str__(self):
        return f"Marka: {self.Marka}, Model: {self.Model}, Faydalı Yük: {self.Faydalı_yük}, Havada Kalma Süresi: {self.Havada_kalma_süresi}, Kanat Açıklığı: {self.Kanat_açıklığı}, Maksimum Kalkış Ağırlığı: {self.Maksimum_kalkış_ağırlığı}"


class Kira(models.Model):
    baslangıc_tarih = models.DateField(default="2010-12-31")
    baslangıc_saat = models.TimeField(default="12:00:00")
    bitiş_tarih = models.DateField(default="2050-12-31")
    bitiş_saat = models.TimeField(default="12:00:00")
    Adet = models.IntegerField(default=0)
    kirayan_üye = models.ForeignKey(User, on_delete=models.CASCADE)
    iha = models.ForeignKey('Iha', on_delete=models.CASCADE, related_name="iha_rentalhistory")


    def __str__(self):
        return f"Tarih: {self.baslangıc_tarih}, Saat: {self.baslangıc_saat}-{self.bitiş_saat}, Kirayan Üye: {self.kirayan_üye}"

class RentalHistory(models.Model):
    baslangıc_tarih = models.DateField()
    baslangıc_saat = models.TimeField()
    bitiş_tarih = models.DateField()
    bitiş_saat = models.TimeField()
    Adet = models.IntegerField()
    kirayan_üye = models.ForeignKey(User, on_delete=models.CASCADE)
    iha = models.ForeignKey('Iha', on_delete=models.CASCADE)

    def __str__(self):
        return f"Tarih: {self.baslangıc_tarih}-{self.bitiş_tarih}, Saat: {self.baslangıc_saat}-{self.bitiş_saat}, Kirayan Üye: {self.kirayan_üye}"
