from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from .forms import *

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
    data = {
        'form': PacienteForm(),
        'log': LoginPaciente(),
        }

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            data['mensaje'] = 'Los datos fueron añadidos correctamente'

    return render(request, 'registration/logReg.html', data)

    
def login(request):   
    data = {}
    
    userN = request.GET.get('username', None)
    pssw = request.GET.get('password', None)

    user = authenticate(username = userN, password = pssw)
    if user is not None:
        login(request, user)
    else:
        data['mensaje'] = 'Error al iniciar sesión'
        return render(request, 'registration/login.html', data)



def appointment(request):
    especialidades = Especialidad.objects.all()
    especialidad_filtrada = request.GET.get('especialidad', None)
    if especialidad_filtrada:
        medicos = Medico.objects.filter(especialidad__nombre_esp=especialidad_filtrada)
    else:
        medicos = Medico.objects.all()
    return render(request, 'core/appointment.html', {'especialidades': especialidades, 'medicos': medicos})
