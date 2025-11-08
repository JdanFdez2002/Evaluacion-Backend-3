from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def foro_list(request):
    posts = Post.objects.all().order_by('-creado') # Ordenar por fecha de creación descendente
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page') #
    page_obj = paginator.get_page(page_number) # Obtener los objetos de la página actual
    return render(request, 'foro/foro_lista.html', {'page_obj': page_obj}) # mostar los posts en la plantilla foro_lista.html