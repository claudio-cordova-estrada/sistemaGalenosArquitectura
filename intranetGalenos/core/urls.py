from django.urls import path, include
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('appointment', appointment, name="appointment"),
    path('contact', contact, name="contact"),
    path('price', price, name="price"),
    path('service', service, name="service"),
    path('team', team, name="team"),
    path('testimonial', testimonial, name="testimonial"),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]

admin.site.site_header = "Administrador"