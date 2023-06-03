from django.urls import path
from . import views

urlpatterns = [
    path('inicio',views.inicio, name='inicio'),
    path('lck', views.lck , name='lck'),
]
