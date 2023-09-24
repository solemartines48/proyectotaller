from django.urls import path 
from MiPrimerApp1 import views 

urlpatterns = [
    path('', views.MiPrimerFuncion, name='mi-primer-funcion'),
]