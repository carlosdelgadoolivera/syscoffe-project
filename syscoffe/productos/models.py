from django.db import models


class Categoria(models.Model):
    # django crea automaticamente la llave primaria en el cmapo id
    nombre = models.CharField(max_length=50)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    es_activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, related_name='productos') # producto_set
    precio = models.FloatField()
    descripcion = models.TextField(max_length=500, blank=True, null=True, default=None)
    imagen = models.ImageField(upload_to='producto/', blank=True, null=True, default=None)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
