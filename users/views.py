from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .RegistrationForm import RegistrationForm


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username =username, password=password)
        if user is not None:
            login(request,user)
            request.session['user_id'] = user.id
            return redirect(reverse('iha:index'))
        else:
             return render(request, "users/login.html",{
                 "message": "Yanlış kullanıcı adı veya şifre"
             })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message" : "Çıkış Yapıldı"
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "users/login.html")
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})
