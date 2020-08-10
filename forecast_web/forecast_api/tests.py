import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Producto, Venta, Forecast



# initialize the APIClient app
client = Client()
# Create your tests here.
class ForecastTest(TestCase):

    def setUp(self):

        ventas = [{"ganancia":"1000"},{"ganancia":"6000"},{"ganancia":"2000"},
            {"ganancia":"15000"},{"ganancia":"30000"},{"ganancia":"37000"},
            {"ganancia":"30000"},{"ganancia":"50000"},{"ganancia":"39000"},
            {"ganancia":"55000"},{"ganancia":"1000000"},{"ganancia":"65000"},
            {"ganancia":"73000"},{"ganancia":"85000"},{"ganancia":"10400000"},
            {"ganancia":"65000"},{"ganancia":"76000"}]

        self.producto_dict = {"categoria":"producto_prueba",
            "nombre":"nombre_prueba", "ventas":ventas,
            "nombreComercio":"comercio_prueba"}
        self.producto = Producto(categoria='producto_prueba',
            nombre_producto='nombre_prueba', ventas=ventas,
            nombre_comercio='comercio_prueba')
        self.producto.save()

    def tearDown(self):
        self.producto.delete()

    def test_get_all(self):

        response = self.client.get(reverse('Forecast'))

        forecast = [f for f in Forecast.objects.filter().values()]
        self.assertEqual(response.json(), forecast)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_producto(self):
        print(json.dumps(self.producto_dict))
        response = self.client.post(reverse('Forecast'), self.producto_dict, content_type='application/json' )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
