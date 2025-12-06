import json
import logging
from urllib.error import URLError
from urllib.request import Request, urlopen

from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Manga

logger = logging.getLogger(__name__)


def _serialize_manga(m):
    fecha_pub = m.fecha_publicacion
    fecha_iso = fecha_pub.isoformat() if hasattr(fecha_pub, "isoformat") else str(fecha_pub)
    return {
        "id": m.id,
        "titulo": m.titulo,
        "autor": m.autor,
        "descripcion": m.descripcion,
        "fecha_publicacion": fecha_iso,
        "portada": m.portada,
    }


@csrf_exempt
def manga_api(request):
    if request.method == "GET":
        data = [_serialize_manga(m) for m in Manga.objects.all()]
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        payload = request.POST
        titulo = payload.get("titulo")
        autor = payload.get("autor", "")
        descripcion = payload.get("descripcion", "")
        fecha_publicacion = payload.get("fecha_publicacion")
        portada = payload.get("portada")
        if not (titulo and fecha_publicacion and portada):
            return JsonResponse(
                {"error": "Faltan campos obligatorios (titulo, fecha_publicacion, portada)"},
                status=400,
            )
        try:
            from datetime import date

            try:
                fecha_obj = date.fromisoformat(fecha_publicacion)
            except ValueError:
                return JsonResponse({"error": "fecha_publicacion debe ser YYYY-MM-DD"}, status=400)

            manga = Manga.objects.create(
                titulo=titulo,
                autor=autor,
                descripcion=descripcion,
                fecha_publicacion=fecha_obj,
                portada=portada,
            )
        except Exception as exc:
            logger.exception("Error creando manga via API")
            return JsonResponse({"error": str(exc)}, status=400)
        return JsonResponse(_serialize_manga(manga), status=201)

    return JsonResponse({"detail": "Método no permitido"}, status=405)


def feed_premium(request):
    is_premium = False
    if request.user.is_authenticated:
        try:
            lector_group = Group.objects.get(name="Lector Premium")
            is_premium = lector_group.user_set.filter(id=request.user.id).exists()
        except Group.DoesNotExist:
            is_premium = False

    mangas = []
    error_msg = None
    if is_premium:
        host = request.get_host()
        port = request.META.get("SERVER_PORT")
        if host.startswith("testserver"):
            host = "127.0.0.1"
            if port and port not in ("80", "443"):
                host = f"{host}:{port}"
        api_url = f"{request.scheme}://{host}{reverse('feed:manga_api')}"
        try:
            req = Request(api_url, headers={"Accept": "application/json"})
            with urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    mangas = json.loads(resp.read().decode("utf-8"))
                else:
                    error_msg = f"API respondió con estado {resp.status}"
        except URLError as exc:
            logger.exception("Error consumiendo API de mangas via HTTP; probando fallback interno")
            try:
                from django.test import Client

                client = Client()
                resp = client.get(reverse("feed:manga_api"))
                if resp.status_code == 200:
                    mangas = json.loads(resp.content.decode("utf-8"))
                else:
                    error_msg = f"API respondió con estado {resp.status_code}"
            except Exception as inner_exc:
                error_msg = f"No se pudo cargar el feed ({inner_exc})"

    context = {
        "mangas": mangas,
        "is_premium": is_premium,
        "error_msg": error_msg,
    }
    return render(request, "feed/premium_feed.html", context)
