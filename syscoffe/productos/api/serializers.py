from rest_framework import serializers
from ..models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

class ProductoBasicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        #fields = ('')
        exclude = ('fecha_creado','fecha_modificado')

