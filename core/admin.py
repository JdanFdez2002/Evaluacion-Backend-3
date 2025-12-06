from django.contrib import admin
from .models import Manga


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "publicado", "creado")
    list_filter = ("publicado", "creado")
    search_fields = ("titulo", "autor", "descripcion")
    readonly_fields = ("creado", "actualizado")
