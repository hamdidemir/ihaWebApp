from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import iha, Kira, RentalHistory
from .forms import RentalForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages


iha.objects = iha.objects
Kira.objects = Kira.objects
RentalHistory.objects = RentalHistory.objects
@login_required
def index(request):
    user_rentals = Kira.objects.filter(kirayan_üye=request.user)  # Filter rentals for the current user
    for rental in user_rentals:
        start_datetime = datetime.combine(rental.baslangıc_tarih, rental.baslangıc_saat)
        end_datetime = datetime.combine(rental.bitiş_tarih, rental.bitiş_saat)
        rental.duration = (end_datetime - start_datetime).total_seconds() / 3600  # Calculate duration in hours
    return render(request, "iha/index.html", {
        "iha": iha.objects.all().order_by("id"),
        "user_rentals": user_rentals,
    })


@login_required
def iha_view(request, iha_id):
    Iha = iha.objects.get(pk = iha_id)
    return render(request, "iha/ihas.html", {
        "iha": Iha
    })


@login_required
def add_rental(request, iha_id):
    Iha = iha.objects.get(pk=iha_id)

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.iha = Iha
            rental.kirayan_üye = request.user
            rental.save()

            # Create a historical record
            history_entry = RentalHistory(
                baslangıc_tarih=rental.baslangıc_tarih,
                baslangıc_saat=rental.baslangıc_saat,
                bitiş_tarih=rental.bitiş_tarih,
                bitiş_saat=rental.bitiş_saat,
                Adet=rental.Adet,
                kirayan_üye=request.user,
                iha=Iha
            )
            history_entry.save()

            return redirect('iha:index')
        else:
            print(form.errors)
    else:
        form = RentalForm()

    return render(request, "iha/ihas.html", {
        "iha": Iha,
        "form": form
    })


@login_required
def cancel_rental(request, rental_id):
    try:
        rental = Kira.objects.get(pk=rental_id)

        # Delete the rental
        rental.delete()

        messages.success(request, "Kiralama başarıyla silindi.")
        return redirect('iha:index')
    except Kira.DoesNotExist:
        messages.error(request, "Kiralama Bulunamadı.")
        return redirect('iha:index')

@login_required
def rental_history(request):
    rental_history = RentalHistory.objects.filter(kirayan_üye=request.user)
    return render(request, "iha/rental_history.html", {
        "rental_history": rental_history
    })

@login_required
def delete_rental_history(request):
    try:
        # Delete all rental history entries for the current user
        RentalHistory.objects.filter(kirayan_üye=request.user).delete()
        messages.success(request, "Kiralama geçmişi başarıyla temizlendi.")
    except Exception as e:
        messages.error(request, "Geçmiş silinirken bira hata meydana geldi.")

    return redirect('iha:rental_history')


