from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def preguntas_frecuentes(request):
    return render(request, 'core/preguntas_frecuentes.html')

def galeria(request):
    return render(request, 'core/galeria.html')