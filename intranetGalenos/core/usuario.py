# En views.py de tu aplicación 'usuarios'
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # El formulario es válido, ahora podemos crear un nuevo usuario
            user = form.save()

            # Loguear al usuario después de crear la cuenta (opcional)
            login(request, user)

            # Redirigir a una página de éxito o a la página de inicio
            return redirect('pagina-exito')
    else:
        form = UserCreationForm()

    return render(request, 'usuarios/registro.html', {'form': form})