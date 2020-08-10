from djongo import models

# Create your models here.
class Venta(models.Model):

    ganancia = models.CharField(max_length=60, blank=True)

    class Meta:
        abstract = True


class Producto(models.Model):

    _id = models.ObjectIdField()
    categoria = models.CharField(max_length=60, blank=True)
    nombre_producto = models.CharField(max_length=60, blank=True)
    ventas = models.ArrayField(model_container=Venta)
    nombre_comercio = models.CharField(max_length=60, blank=True)


class Forecast(models.Model):

    categoria = models.CharField(max_length=60, blank=True)
    producto = models.CharField(max_length=60, blank=True)
    cantidad = models.CharField(max_length=60, blank=True)
    ganancia = models.CharField(max_length=60, blank=True)
    nombre = models.CharField(max_length=60, blank=True)
