from django.contrib import admin
from .models import Post, Categoria, Comentario


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1
    fields = ("autor", "contenido", "creado")
    readonly_fields = ("creado", "actualizado")


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")
    list_display = ("titulo", "categoria", "creado")
    list_display_links = ("titulo",)
    list_filter = ("categoria", "creado")
    search_fields = ("titulo", "contenido")
    ordering = ("-creado",)
    date_hierarchy = "creado"
    list_per_page = 10
    list_editable = ("categoria",)
    fieldsets = (
        ("Contenido", {"fields": ("titulo", "contenido", "foto")}),
        ("Clasificacion y Metadatos", {
            "fields": ("categoria", "creado", "actualizado"),
        }),
    )
    inlines = [ComentarioInline]
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

admin.site.site_header = "KapowStore - Panel de Administracion"
admin.site.site_title = "KapowStore Admin"
admin.site.index_title = "Administracion de KapowStore"
