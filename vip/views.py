from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,"vip/login.html")

def signup(request):
    return render(request,"vip/signup.html")

def home(request):
    return render(request,"vip/base.html")


def wdraw(request):
    return render(request,"vip/wdraw.html")

def promo(request):
    return render(request,"vip/promo.html")

def assets(request):
    return render(request,"vip/assets.html")



