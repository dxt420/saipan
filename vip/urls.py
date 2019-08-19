from django.urls import path
from . import views


app_name = 'vip'

urlpatterns = [
    path('', views.auth , name="auth"),
    path('auth', views.auth , name="auth"),
    path('home', views.home , name="home"),
    path('verification', views.verification , name="verification"),
]