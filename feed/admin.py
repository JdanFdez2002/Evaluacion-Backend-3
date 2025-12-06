from django.contrib import admin

from .models import Manga


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_publicacion", "portada", "creado")
    list_filter = ("fecha_publicacion", "creado")
    search_fields = ("titulo", "autor", "descripcion")
    readonly_fields = ("creado",)
