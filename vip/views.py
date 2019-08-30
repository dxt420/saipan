from django.shortcuts import render
from . forms import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse

# Create your views here.


def signin(request):
    return render(request,"registration/login.html")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    
    return HttpResponseRedirect(reverse('vip:signin'))

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            
            print("Yess")
            return HttpResponseRedirect(reverse('vip:home'))
            
        else:
            context = {
                'errors':'error'
            }
            print("Nope")
            return render(request,"registration/login.html",context)
    else:
        print("Well yes but actually no")
        return render(request,"registration/login.html")

def register(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        

        if form.is_valid():
            form.save()
            # user = form.save()
            # user.phone = request.POST['phone']
            # user.save()
           
            # messages.success(request, "Successfully added")
         
            return HttpResponseRedirect(reverse('vip:login'))
       
            
    
    context = {'form': form}

    return render(request,"vip/signup.html", context)

def signup(request):
    return render(request,"vip/signup.html")

@login_required
def home(request):
    return render(request,"vip/base.html")


def wdraw(request):
    return render(request,"vip/wdraw.html")

def promo(request):
    return render(request,"vip/promo.html")

def assets(request):
    return render(request,"vip/assets.html")

def pin(request):
    return render(request,"vip/pin.html")


    



