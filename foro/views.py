from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Categoria

def foro_list(request):
    queryset = Post.objects.all()
    categoria_id = request.GET.get('categoria')
    q = request.GET.get('q')

    if categoria_id:
        queryset = queryset.filter(categoria_id=categoria_id)

    if q:
        queryset = queryset.filter(
            Q(titulo__icontains=q) | Q(contenido__icontains=q)
        )

    queryset = queryset.order_by('-creado')

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    params = request.GET.copy()
    params.pop('page', None)
    querystring = params.urlencode()

    context = {
        'page_obj': page_obj,
        'categorias': Categoria.objects.all().order_by('nombre'),
        'categoria_actual': categoria_id,
        'q': q or '',
        'querystring': querystring,
    }
    return render(request, 'foro/foro_lista.html', context)
