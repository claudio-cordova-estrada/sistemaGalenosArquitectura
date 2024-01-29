from django import forms
from django.forms import ModelForm
from .models import *

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'email', 'password', 'apellido_paterno', 
                  'apellido_materno', 'telefono', 'rut_paciente', 'dv_paciente', 'direccion']