from django.shortcuts import render, redirect
from .models import usuario as Usuarios, Genero 
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.

def inicio(request):
    context={}
    return render(request, 'inicio.html',context)

def lck(request):
    context={}
    return render(request, 'lck.html',context)

def quizgeng(request):
    context={}
    return render(request, 'quiz_Gen.G.html',context)

def quiz(request):
    context={}
    return render(request, 'quiz.html',context)

def t1(request):
    context={}
    return render(request, 't1.html',context)

def register(request):
    context={}
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Registro completado")
            return redirect(to="/")
        data["form"]=formulario
    return render(request, 'registration/register.html',data)