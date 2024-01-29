from django import forms
from django.forms import ModelForm
from .models import *

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'email', 'password', 'apellido_paterno', 
                  'apellido_materno', 'telefono', 'rut_paciente', 'dv_paciente', 'direccion']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class LoginPaciente(ModelForm):
    class Meta:
        model = Paciente
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})