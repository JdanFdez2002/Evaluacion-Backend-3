from django.utils import timezone
from foro.models import Categoria, Post


def kapow_globals(request):
    return {
        "site_name": "KapowStore",
        "site_tagline": "Tu bahia mangaka",
        "current_year": timezone.now().year,
        "categorias_nav": Categoria.objects.all().order_by("nombre"),
        "total_posts": Post.objects.count(),
        "social_links": {
            "facebook": "https://www.facebook.com/",
            "instagram": "https://www.instagram.com/",
            "twitter": "https://x.com/",
        },
    }
