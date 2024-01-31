from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=90)
    password = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    telefono = models.IntegerField()

    def __str__(self):
        return str(self.email)
    
    class Meta:
        abstract = True
    
class Paciente(Usuario):
    rut_paciente = models.IntegerField()
    dv_paciente = models.CharField(max_length=1)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return str(self.rut_paciente)
    
class Especialidad(models.Model):
    nombre_esp = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_esp

class Medico(Usuario):
    rut_medico = models.IntegerField()
    dv_medico = models.CharField(max_length=1)
    especialidad = models.ForeignKey(Especialidad, on_delete=CASCADE)

    def __str__(self):
        return str(self.rut_medico)
    
class Horario(models.Model):
    rut_medico = models.ForeignKey(Medico, on_delete=CASCADE)
    jornada = models.CharField(max_length=200)
    dias_semana = models.CharField(max_length=200)
    finalizacion_contrato = models.DateTimeField()
    
    def __str__(self):
        return str(self.rut_medico)
    


class Secretaria(Usuario):
    rut_secretaria = models.IntegerField()
    dv_secretaria = models.CharField(max_length=1)

    def __str__(self):
        return str(self.rut_secretaria)

class Atencion(models.Model):
    rut_paciente = models.ForeignKey(Paciente, on_delete=CASCADE)
    rut_medico = models.ForeignKey(Medico, on_delete=CASCADE)
    fecha = models.DateField()
    hora_inicio = models.CharField(max_length=5)
    hora_fin = models.CharField(max_length=5)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)
    
class Boleta(models.Model):
    atencion_id = models.ForeignKey(Atencion, on_delete=CASCADE)
    total = models.IntegerField()
    descuento = models.IntegerField()
    
    def __str__(self):
        return str(self.id)