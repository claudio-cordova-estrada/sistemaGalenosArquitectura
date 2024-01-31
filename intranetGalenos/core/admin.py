from django.contrib import admin
from .models import *

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'password', 'apellido_paterno', 'apellido_materno', 'telefono', 'rut_paciente', 'dv_paciente', 'direccion']
    search_fields = ['email', 'telefono', 'rut_paciente']
    list_per_page = 15

class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'password', 'apellido_paterno', 'apellido_materno', 'telefono', 'rut_medico', 'dv_medico', 'especialidad']
    search_fields = ['email', 'telefono', 'rut_medico', 'especialidad']
    list_per_page = 15

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_esp']
    list_per_page = 15


class HorarioAdmin(admin.ModelAdmin):
    list_display = ['rut_medico', 'jornada', 'dias_semana', 'finalizacion_contrato']
    search_fields = ['rut_medico', 'finalizacion_contrato']
    list_per_page = 15

class SecretariaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'password', 'apellido_paterno', 'apellido_materno', 'telefono', 'rut_secretaria', 'dv_secretaria']
    search_fields = ['email', 'telefono', 'rut_secretaria']
    list_per_page = 15

class AtencionAdmin(admin.ModelAdmin):
    list_display = ['rut_paciente', 'rut_medico', 'fecha', 'hora_inicio', 'hora_fin', 'estado']
    search_fields = ['rut_paciente', 'rut_medico', 'fecha', 'estado']
    list_per_page = 15

class BoletaAdmin(admin.ModelAdmin):
    list_display = ['atencion_id', 'total', 'descuento']
    list_filter = ['atencion_id']
    list_per_page = 15

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Secretaria, SecretariaAdmin)
admin.site.register(Atencion, AtencionAdmin)
admin.site.register(Boleta, BoletaAdmin)