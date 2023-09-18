from django.contrib import admin
from .models import iha, Kira, RentalHistory

class IhaAdmin(admin.ModelAdmin):
    list_display = ('Marka', 'Model', 'Faydalı_yük', 'Havada_kalma_süresi', 'Kanat_açıklığı', 'Maksimum_kalkış_ağırlığı')
    list_filter = ('Marka', 'Model')
    search_fields = ('Marka', 'Model')
    list_per_page = 20  # Number of items to display per page

class KiraAdmin(admin.ModelAdmin):
    list_display = ('baslangıc_tarih', 'baslangıc_saat', 'bitiş_tarih', 'bitiş_saat', 'Adet', 'kirayan_üye', 'iha')
    list_filter = ('baslangıc_tarih', 'kirayan_üye')
    search_fields = ('kirayan_üye__username', 'iha__Marka', 'iha__Model')  # Use double underscores for related fields
    list_per_page = 20  # Number of items to display per page

    # Add a date hierarchy for easy navigation by date
    date_hierarchy = 'baslangıc_tarih'

    # Customize the ordering of items in the admin list view
    ordering = ('-baslangıc_tarih', '-baslangıc_saat')

class RentalHistoryAdmin(admin.ModelAdmin):
    list_display = ('baslangıc_tarih', 'baslangıc_saat', 'bitiş_tarih', 'bitiş_saat', 'Adet', 'kirayan_üye', 'iha')
    list_filter = ('baslangıc_tarih', 'kirayan_üye')
    search_fields = ('kirayan_üye__username', 'iha__Marka', 'iha__Model')  # Use double underscores for related fields
    list_per_page = 20  # Number of items to display per page

    # Add a date hierarchy for easy navigation by date
    date_hierarchy = 'baslangıc_tarih'

    # Customize the ordering of items in the admin list view
    ordering = ('-baslangıc_tarih', '-baslangıc_saat')

# Register your models with the custom admin options
admin.site.register(iha, IhaAdmin)
admin.site.register(Kira, KiraAdmin)
admin.site.register(RentalHistory, RentalHistoryAdmin)
