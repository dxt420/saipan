from django.urls import path
from . import views


app_name = 'vip'

urlpatterns = [
    path('', views.signup , name="signup"),
    path('login', views.login , name="login"),
    path('signup', views.signup , name="signup"),
    path('home', views.home , name="home"),
    path('wdraw', views.wdraw , name="wdraw"),
    path('promo', views.promo , name="promo"),
    path('assets', views.assets , name="assets"),
]