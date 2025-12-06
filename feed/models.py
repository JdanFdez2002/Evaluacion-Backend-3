from django.db import models


class Manga(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150, blank=True)
    descripcion = models.TextField(blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    portada = models.URLField(help_text="URL de la imagen/portada")
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo
