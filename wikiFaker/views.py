from django.shortcuts import render
from .models import usuario as XD, Genero
from django.shortcuts import redirect

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


def login(request):
    
        return render(request, 'login.html')

def register(request):
    if request.method != "POST":
        # no es un POST por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'register.html', context)
    else:
        print("--->>>> llego al else de addAlumnos crea el objeto ")
        # Es un POST, por lo tanto se recuperan los datos del formulario
        # y se graban en la tabla
        usuario = request.POST["usuario"]
        genero = request.POST["genero"]
        correo = request.POST["correo"]
        contraseña= request.POST["contraseña"]
        
        objGenero = Genero.objects.get(id_genero=genero)
        obj = XD.objects.create(
                                    usuario=usuario,
                                    id_genero=objGenero,
                                    correo=correo,
                                    contraseña=contraseña)
        obj.save()
        context = {"mensaje": "OK, datos grabados..."}
        return render(request, 'register.html', context)