from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
#from .forms import TaskForm
#from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators  import login_required

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    else:
        print("ok")
        return render(request, "home.html")

def kevin(request):
    if request.method == "GET":
        return render(request, "kevin.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                Usuario = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                Usuario.save()
                login(request, Usuario)
                return redirect("cotizar")
            except:
                return render(request, "singup.html", {
                    "formulario": UserCreationForm,
                    "error": "El usuario ya existe"
                })
        else:
             return render(request, "kevin.html", {"error": "Error"})

def cotizar(request):
    return render(request, "cotizar.html")