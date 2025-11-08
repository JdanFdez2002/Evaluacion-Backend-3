from django.utils import timezone
from foro.models import Categoria, Post


def kapow_globals(request):
    """
    Variables globales coherentes con KapowStore, disponibles en todas las plantillas.
    Evita lógica pesada; lecturas simples/ordenadas.
    """
    return {
        "site_name": "KapowStore",
        "site_tagline": "Tu bahia mangaka",
        "current_year": timezone.now().year,
        # Navegación: categorías (útil para menús/filtros globales)
        "categorias_nav": Categoria.objects.all().order_by("nombre"),
        # Métrica simple para usar en banners o badges
        "total_posts": Post.objects.count(),
        # Enlaces sociales globales (footer/header)
        "social_links": {
            "facebook": "https://www.facebook.com/",
            "instagram": "https://www.instagram.com/",
            "twitter": "https://x.com/",
        },
    }

