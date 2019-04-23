from rest_framework.routers import DefaultRouter
from .views import CategoriaApiView, CategoriaDosApiView

router = DefaultRouter()
"""
dominio.com/api/v1/nodo/endpoint/ (list [get], create [post])
dominio.com/api/v1/nodo/endpoint/{pk} (retrieve [get], update [put / patch], destroy [delete]
"""
router.register(r'categoria', CategoriaApiView, base_name='categoria')
router.register(r'categoria-dos', CategoriaDosApiView, base_name='categoria-dos')

urlpatterns = router.urls
