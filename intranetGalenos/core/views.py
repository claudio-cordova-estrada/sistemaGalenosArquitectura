from django.shortcuts import render
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
        }

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            data['mensaje'] = 'Los datos fueron añadidos correctamente'
    else:
        form = PacienteForm()
        data['mensaje'] = 'Los datos no pudieron ser añadidos'

    return render(request, 'registration/logReg.html', data)