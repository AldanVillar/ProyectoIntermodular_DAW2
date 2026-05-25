from django.contrib import admin
from .models import Genero, Plataforma, Juego, Noticia


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'precio', 'genero', 'plataforma', 'destacado', 'top_ventas', 'novedad', 'en_descuento', 'stock']
    list_filter = ['genero', 'plataforma', 'destacado', 'top_ventas', 'novedad', 'en_descuento']
    search_fields = ['titulo']
    list_editable = ['destacado', 'top_ventas', 'novedad', 'en_descuento', 'stock']


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    search_fields = ['titulo']
