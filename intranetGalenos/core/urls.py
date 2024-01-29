from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('appointment', appointment, name="appointment"),
    path('contact', contact, name="contact"),
    path('logReg', logReg, name="logReg"),
    path('price', price, name="price"),
    path('service', service, name="service"),
    path('team', team, name="team"),
    path('testimonial', testimonial, name="testimonial"),
]

admin.site.site_header = "Administrador"