from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
]

admin.site.site_header = "Administrador"