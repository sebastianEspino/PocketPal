from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def login(request):
    # Renderiza la plantilla 'index.html' y la devuelve como respuesta
    return render(request, 'login/login.html') 

def forgot_password(request):
    return render(request, 'login/Passwordreset.html') 