from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def preguntas_frecuentes(request):
    return render(request, 'core/preguntas_frecuentes.html')

def galeria(request):
    return render(request, 'core/galeria.html')


def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)


def custom_404_catchall(request, path=None):
    return render(request, 'core/404.html', status=404)

