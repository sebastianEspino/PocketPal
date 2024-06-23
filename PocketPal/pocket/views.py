from django.contrib import messages
from .models import *
from django.shortcuts import render,redirect
from .crypt import *
# Create your views here.

def login(request):
    return render(request, 'login/login.html') 

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            u = Usuario(
                nombre = name,
                correo = correo,
                password = hash_password(password)
                
            )

            u.save()
            messages.success(request,'Usuario creado exitosamente')
            return redirect('login')

        except Exception as e:
            messages.error(request, "Error al momento de registrarse...")
            return redirect("login")
        

def logueo(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
                u = Usuario.objects.get(correo=correo)
                if verify_password(password,u.password):
                    request.session["logueo"]={
                        "nombre":u.nombre,
                        "correo":u.correo
                    }
                    request.session["carrito"] = []
                    request.session["items"] = 0
                    messages.success(request, f"Bienvenido {u.nombre}!!")
                    print(u.password)
                    return redirect("index")
                else:
                    messages.error(request, "Error: Usuario o contraseña incorrectos...")
                    return redirect("login")
        except Exception as e:
            messages.error(request, "Error: Usuario o contraseña incorrectos...")
            return redirect("login")
        
def forgot_password(request):
    return render(request, 'login/Passwordreset.html') 