from django.contrib import admin
from .models import Post, Categoria, Comentario

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('titulo', 'categoria', 'creado')
    list_filter = ('categoria', 'creado')
    search_fields = ('titulo', 'contenido')


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
