from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, is_valid_path

from .forms import EditorRegistroForm, LectorRegistroForm


def home(request):
    return render(request, "core/home.html")


def quienes_somos(request):
    return render(request, "core/quienes_somos.html")


def preguntas_frecuentes(request):
    return render(request, "core/preguntas_frecuentes.html")


def galeria(request):
    return render(request, "core/galeria.html")


def custom_404(request, exception):
    return render(request, "core/404.html", status=404)


def custom_404_catchall(request, path=None):
    # Rehabilita APPEND_SLASH cuando el patrón catch-all captura rutas sin la barra final.
    if settings.APPEND_SLASH and path and not request.path_info.endswith("/"):
        slash_path = f"{request.path_info}/"
        urlconf = getattr(request, "urlconf", settings.ROOT_URLCONF)
        if is_valid_path(slash_path, urlconf=urlconf):
            return HttpResponsePermanentRedirect(
                request.get_full_path(force_append_slash=True)
            )
    return render(request, "core/404.html", status=404)


def _ensure_group_with_permissions(group_name, perm_codenames):
    """
    Obtiene o crea el grupo y garantiza los permisos del modelo Manga de la app feed.
    """
    group, created = Group.objects.get_or_create(name=group_name)
    perms = Permission.objects.filter(
        codename__in=perm_codenames, content_type__app_label="feed"
    )
    if created:
        group.permissions.set(perms)
    else:
        missing = perms.exclude(id__in=group.permissions.values_list("id", flat=True))
        if missing:
            group.permissions.add(*missing)
    return group


def _registrar_usuario(request, form_class, group_name, perm_codenames, template_name):
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # acceso a panel de administración
            user.save()
            group = _ensure_group_with_permissions(group_name, perm_codenames)
            group.user_set.add(user)
            return redirect(reverse("registro_exito"))
    else:
        form = form_class()

    return render(request, template_name, {"form": form})


def registro_editor(request):
    perm_codenames = ["add_manga", "change_manga", "delete_manga", "view_manga"]
    return _registrar_usuario(
        request,
        EditorRegistroForm,
        "Editor",
        perm_codenames,
        "core/registro_editor.html",
    )


def registro_lector(request):
    perm_codenames = ["view_manga"]
    return _registrar_usuario(
        request,
        LectorRegistroForm,
        "Lector Premium",
        perm_codenames,
        "core/registro_lector.html",
    )


def registro_exito(request):
    return render(request, "core/registro_exito.html")
