from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from ..models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoBasicoSerializer


class CategoriaApiView(ModelViewSet):
    """ Vista de api de categoria utilizanod ModelViewset
    list - GET
    retrieve - GET (pk)
    create - POST
    update - PUT / PATCH
    destroy - DELETE
    """
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny,]

class CategoriaDosApiView(ViewSet):

    def list(self, request, *args, **kwargs):
        queryset = Categoria.objects.all()
        serializer = CategoriaSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductoApiView(ModelViewSet):
    serializer_class = ProductoBasicoSerializer
    queryset = Producto.objects.all()
