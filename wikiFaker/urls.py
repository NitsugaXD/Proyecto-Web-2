from django.urls import path
from . import views

urlpatterns = [
    path('inicio',views.inicio, name='inicio'),
    path('lck', views.lck , name='lck'),
    path('quiz_Gen.G', views.quizgeng , name='quiz_Gen.G'),
    path('quiz', views.quiz , name='quiz'),
    path('t1', views.t1 , name='t1'),
]
