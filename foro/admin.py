from django.contrib import admin
from .models import Post, Categoria, Comentario

# Register your models here.

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1
    fields = ("autor", "contenido", "creado")
    readonly_fields = ("creado", "actualizado")


class PostAdmin(admin.ModelAdmin):
    # 1) Campos de solo lectura
    readonly_fields = ("creado", "actualizado")

    # 2) Columnas mostradas en lista
    list_display = ("titulo", "categoria", "creado")

    # 3) Enlaces en lista
    list_display_links = ("titulo",)

    # 4) Filtros laterales
    list_filter = ("categoria", "creado")

    # 5) Búsqueda por texto
    search_fields = ("titulo", "contenido")

    # 6) Orden por defecto
    ordering = ("-creado",)

    # 7) Jerarquía por fecha
    date_hierarchy = "creado"

    # 8) Paginación en el changelist
    list_per_page = 10

    # 9) Edición rápida desde la lista
    list_editable = ("categoria",)

    # 10) Agrupar campos en el formulario
    fieldsets = (
        ("Contenido", {
            "fields": ("titulo", "contenido", "foto"),
        }),
        ("Clasificación y Metadatos", {
            "fields": ("categoria", "creado", "actualizado"),
        }),
    )

    # 11) Inlines de comentarios
    inlines = [ComentarioInline]

    # 12) Botones de guardado arriba
    save_on_top = True


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('nombre', 'creado')
    search_fields = ('nombre',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('post', 'autor', 'creado')
    list_filter = ('creado',)
    search_fields = ('autor', 'contenido')


admin.site.register(Post, PostAdmin)

# Branding del panel para respetar la temática KapowStore
admin.site.site_header = "KapowStore • Panel de Administración"
admin.site.site_title = "KapowStore Admin"
admin.site.index_title = "Administración de KapowStore"
