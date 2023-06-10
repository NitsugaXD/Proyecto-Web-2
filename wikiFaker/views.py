from django.shortcuts import render

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