from django.shortcuts import render
from .models import AlumnoT, Frase
# Create your views here.

def Index_vista(request):
    mis_alumnos=AlumnoT.objects.all().order_by("id") #nuevo + diccionario
    return render(request,"index.html",{"mis_alumnos":mis_alumnos})
    