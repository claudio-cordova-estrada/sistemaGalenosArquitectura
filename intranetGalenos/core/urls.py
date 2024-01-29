from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('appointment', appointment, name="appointment"),
    path('contact', contact, name="contact"),
    path('', logReg, name="logReg"),
    path('', price, name="price"),
    path('', service, name="service"),
    path('', team, name="team"),
    path('', testimonial, name="testimonial"),
]

admin.site.site_header = "Administrador"