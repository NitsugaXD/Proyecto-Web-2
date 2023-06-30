from django.urls import path
from .views import inicio,lck,quizgeng,t1,register,quiz

urlpatterns = [
    path('',inicio, name=''),
    path('lck', lck , name='lck'),
    path('quiz_Gen.G', quizgeng , name='quiz_Gen.G'),
    path('quiz', quiz , name='quiz'),
    path('t1', t1 , name='t1'),
    path('register', register , name='register'),
]
