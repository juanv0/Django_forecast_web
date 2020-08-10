from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.generic import View
from .models import Venta, Forecast, Producto
from .forecasting_controller import get_forecast_arima, get_forecast_xgboost

# Create your views here.
#class Based View handles get and post to /forecast
class ForecastView(View):

    def get(self, request, *args, **kwargs):
        #Serializing the queryset, that quey is equal to db.Forecast.find()
        #i cast the query set into a list to be serialized
        forecast = [f for f in Forecast.objects.filter().values()]
        #i have to put safe = False, to be able to serlialize the json list
        return JsonResponse(forecast, safe = False)

    def post(self, request, *args, **kwargs):
        #serialize request body
        req = json.loads(request.body.decode())
        #Build our Product Model with request values
        #Note that ventas(an array) fills automatically
        producto = Producto(categoria=req['categoria'],
            nombre_producto=req['nombre'], ventas=req['ventas'],
            nombre_comercio=req['nombreComercio'])
        #save in mongoDB
        producto.save()
        #call methods to forecast sales
        arima = get_forecast_arima(req['ventas'])
        xgboost = get_forecast_xgboost(req['ventas'])
        #define a Json response
        dict_resp={}
        dict_resp['categoria'] = req['categoria']
        dict_resp['producto'] = req['nombre']
        dict_resp['cantidad'] = None
        dict_resp['ganancia'] = str(xgboost[0])
        dict_resp['nombre'] = req['nombreComercio']
        #creating and saving forecas model in db
        forecast = Forecast(categoria=req['categoria'],producto=req['nombre'],
            cantidad=None, ganancia=str(xgboost[0]), nombre=req['nombreComercio'])
        forecast.save()

        return JsonResponse(dict_resp)
