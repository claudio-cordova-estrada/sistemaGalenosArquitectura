from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
import time

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def appointment(request):
    return render(request, 'core/appointment.html')

def contact(request):
    return render(request, 'core/contact.html')

def price(request):
    return render(request, 'core/price.html')

def service(request):
    return render(request, 'core/service.html')

def team(request):
    return render(request, 'core/team.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')

def logReg(request):
    return render(request, 'registration/logReg.html')

    
def login(request):   
    data = {
        'form': 'holaxd',
    }
    return render(request, 'core/login.html', data)


def appointment(request):
    especialidades = Especialidad.objects.all()
    especialidad_filtrada = request.GET.get('especialidad', None)
    if especialidad_filtrada:
        medicos = Medico.objects.filter(especialidad__nombre_esp=especialidad_filtrada)
    else:
        medicos = Medico.objects.all()
    return render(request, 'core/appointment.html', {'especialidades': especialidades, 'medicos': medicos})


def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        
        apellido_paterno = request.POST['apellido_paterno']
        apellido_materno = request.POST['apellido_materno']
        telefono = request.POST['telefono']
        rut_paciente = request.POST['rut_paciente']
        dv_paciente = request.POST['dv_paciente']
        direccion = request.POST['direccion']
        password = make_password(request.POST['password'])
        paciente = Paciente(nombre=nombre, email=email, password=password, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, telefono=telefono,
                            rut_paciente=rut_paciente, dv_paciente=dv_paciente, direccion=direccion)
        paciente.save()
        messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
    return render(request, 'core/registro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        success = False

        try:
            paciente = Paciente.objects.get(email=email)
            if check_password(password, paciente.password):
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('appointment')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Paciente.DoesNotExist:
            messages.error(request, 'No se encontró un usuario con este correo electrónico.')

    return render(request, 'core/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('core/login.html')