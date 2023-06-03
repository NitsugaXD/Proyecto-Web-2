from django.shortcuts import render

# Create your views here.

def inicio(request):
    context={}
    return render(request, 'wikiFaker/inicio.html',context)

def lck(request):
    context={}
    return render(request, 'wikiFaker/lck.html',context)

def quizgeng(request):
    context={}
    return render(request, 'wikiFaker/quiz_Gen.G.html',context)

def quiz(request):
    context={}
    return render(request, 'wikiFaker/quiz.html',context)

def t1(request):
    context={}
    return render(request, 'wikiFaker/t1.html',context)