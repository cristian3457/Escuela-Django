from django.shortcuts import render, redirect
from .models import Usuario
from Profesor.models import Profesor
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.

def iniciarSesion(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(username=usuario, password=password)
        if user is not None:
            if user.tipo != 'ADMINISTRADOR':
                if user.tipo == 'ALUMNO':
                    login(request, user)
                    return redirect('/cargaAcademica/')
                elif user.tipo == 'DOCENTE':
                    login(request, user)
                    return redirect('/cargaProfesor/')
        else:
            return redirect("/?novalido")
         
    return render(request,'login.html')

def home(request):
    
    return render(request,'home.html')

def cerrarSesion(request):
    logout(request)
    return redirect('/')