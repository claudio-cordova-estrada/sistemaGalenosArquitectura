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
            
        email = request.GET.get('email', '')
        password = request.GET.get('password', '')

    return render(request, 'registration/logReg.html', data)

def verificacion(request):
    data = {}
    loginCon = False
    
    email = request.GET.get('email', '')
    password = request.GET.get('password', '')
    
    try:
        usuario = Usuario.object.get(email=email, password=password)
        loginCon = True
        return loginCon
    except Usuario.DoesNotExist:
        data['mensaje'] = 'Usuario no encontrado'
        return loginCon
    
def login(request):
<<<<<<< HEAD
    data = {
        'form': LoginPaciente()
    }

    user = LoginPaciente(request.POST)

    user = authenticate(request, user)
    if user is not None:
        login(request, user)
        redirect(home)
    else:
        redirect('/')

    return render(request, 'registration/login.html')

=======
    return render(request, 'registration/login.html')



def appointment(request):
    especialidades = Especialidad.objects.all()
    especialidad_filtrada = request.GET.get('especialidad', None)
    if especialidad_filtrada:
        medicos = Medico.objects.filter(especialidad__nombre_esp=especialidad_filtrada)
    else:
        medicos = Medico.objects.all()
    return render(request, 'core/appointment.html', {'especialidades': especialidades, 'medicos': medicos})
>>>>>>> 1653afb14b4de4c5ea8bcd038fb75590bb0d9888
