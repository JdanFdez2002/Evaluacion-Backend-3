from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('preguntas-frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('galeria/', views.galeria, name='galeria'),
    path('registro/editor/', views.registro_editor, name='registro_editor'),
    path('registro/lector/', views.registro_lector, name='registro_lector'),
    path('registro/exito/', views.registro_exito, name='registro_exito'),
]
