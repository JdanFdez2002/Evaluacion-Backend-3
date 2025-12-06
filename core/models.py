from django.db import models


class Manga(models.Model):
    """
    Representa contenido principal del sitio (manga/capítulo).
    """
    titulo = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True)
    autor = models.CharField(max_length=120, blank=True)
    publicado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo
