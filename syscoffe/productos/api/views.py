from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from ..models import Categoria, Producto
from .serializers import CategoriaSerializer


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


class CategoriaDosApiView(ViewSet):

    def list(self, request, *args, **kwargs):
        queryset = Categoria.objects.all()
        serializer = CategoriaSerializer(queryset, many=True)
        return Response(serializer.data)


