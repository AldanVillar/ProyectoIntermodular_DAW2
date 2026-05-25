from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Plataforma(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    precio_original = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    imagen = models.CharField(max_length=300)
    fecha_lanzamiento = models.DateField()
    stock = models.PositiveIntegerField(default=0)

    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, related_name='juegos')
    plataforma = models.ForeignKey(Plataforma, on_delete=models.SET_NULL, null=True, related_name='juegos')

    destacado = models.BooleanField(default=False)
    top_ventas = models.BooleanField(default=False)
    novedad = models.BooleanField(default=False)
    en_descuento = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen = models.CharField(max_length=300, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
