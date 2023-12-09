from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index, name='index'),
    path("home",views.home, name='home'),
    path("login",views.login, name='contact'),
    path("work",views.work, name='aboutme'),
    path("request",views.request, name='request'),
    path("forget",views.forget, name='forget')
    
]
