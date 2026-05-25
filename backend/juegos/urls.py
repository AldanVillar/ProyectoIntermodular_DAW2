from rest_framework.routers import DefaultRouter
from .views import GeneroViewSet, PlataformaViewSet, JuegoViewSet, NoticiaViewSet

router = DefaultRouter()
router.register(r'generos', GeneroViewSet, basename='genero')
router.register(r'plataformas', PlataformaViewSet, basename='plataforma')
router.register(r'juegos', JuegoViewSet, basename='juego')
router.register(r'noticias', NoticiaViewSet, basename='noticia')

urlpatterns = router.urls
