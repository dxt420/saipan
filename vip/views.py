from django.shortcuts import render

# Create your views here.


def auth(request):
    return render(request,"vip/auth.html")

def home(request):
    return render(request,"vip/base.html")

def verification(request):
    return render(request,"vip/verification.html")