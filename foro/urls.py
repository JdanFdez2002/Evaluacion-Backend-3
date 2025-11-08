from django.urls import path
from . import views

app_name = 'foro'

urlpatterns = [
    path('', views.foro_list, name='lista'),
]

