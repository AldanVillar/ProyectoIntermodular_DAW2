from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Genero, Plataforma, Juego, Noticia
from .serializers import GeneroSerializer, PlataformaSerializer, JuegoSerializer, NoticiaSerializer


class GeneroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class PlataformaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer


class JuegoViewSet(viewsets.ModelViewSet):
    serializer_class = JuegoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descripcion']
    ordering_fields = ['precio', 'fecha_lanzamiento', 'titulo']

    def get_queryset(self):
        queryset = Juego.objects.select_related('genero', 'plataforma').all()

        destacado = self.request.query_params.get('destacado')
        top_ventas = self.request.query_params.get('top_ventas')
        novedad = self.request.query_params.get('novedad')
        en_descuento = self.request.query_params.get('en_descuento')
        genero_id = self.request.query_params.get('genero')
        plataforma_id = self.request.query_params.get('plataforma')

        if destacado == 'true':
            queryset = queryset.filter(destacado=True)
        if top_ventas == 'true':
            queryset = queryset.filter(top_ventas=True)
        if novedad == 'true':
            queryset = queryset.filter(novedad=True)
        if en_descuento == 'true':
            queryset = queryset.filter(en_descuento=True)
        if genero_id:
            queryset = queryset.filter(genero_id=genero_id)
        if plataforma_id:
            queryset = queryset.filter(plataforma_id=plataforma_id)

        return queryset


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.order_by('-fecha')
    serializer_class = NoticiaSerializer
