from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import usuarioPrincipalLoginForm, MiembroNuevoForm

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = usuarioPrincipalLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirige a 'dashboard'
            else:
                messages.error(request, 'Credenciales inválidas')
                return render(request, 'usuarios/login.html', {'form': form})
    else:
        form = usuarioPrincipalLoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


# Vista de registro de miembros
def registro_view(request):
    if request.method == 'POST':
        form = MiembroNuevoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso')
            return redirect('inicio')  # Redirigir al inicio o a alguna otra página después del registro
        else:
            messages.error(request, 'Datos inválidos')
            return render(request, 'usuarios/registro.html', {'form': form})
    else:
        form = MiembroNuevoForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista de registro de usuarios principales
def registro_principal_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Validaciones
        if password != password_confirm:
            messages.error(request, "Las contraseñas no coinciden.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
        else:
            try:
                validate_password(password)  # Validación de la contraseña
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Usuario principal registrado exitosamente.")
                return redirect('login')  # Redirige al inicio de sesión
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request, error)  # Mostrar los errores de validación de contraseña
    return render(request, 'usuarios/registro_principal.html')

# Vista de inicio
def inicio(request):
    return render(request, 'usuarios/inicio.html')

# Vista de Dashboard
def dashboard(request):
    return render(request, 'usuarios/dashboard.html')  # Asegúrate de crear la plantilla 'dashboard.html'
