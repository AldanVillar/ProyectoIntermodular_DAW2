from rest_framework import serializers
from .models import Genero, Plataforma, Juego, Noticia


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nombre']


class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ['id', 'nombre']


class JuegoSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer(read_only=True)
    plataforma = PlataformaSerializer(read_only=True)
    genero_id = serializers.PrimaryKeyRelatedField(
        queryset=Genero.objects.all(), source='genero', write_only=True
    )
    plataforma_id = serializers.PrimaryKeyRelatedField(
        queryset=Plataforma.objects.all(), source='plataforma', write_only=True
    )

    class Meta:
        model = Juego
        fields = [
            'id', 'titulo', 'descripcion', 'precio', 'precio_original',
            'imagen', 'fecha_lanzamiento', 'stock',
            'genero', 'genero_id', 'plataforma', 'plataforma_id',
            'destacado', 'top_ventas', 'novedad', 'en_descuento',
        ]


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'contenido', 'imagen', 'fecha']
