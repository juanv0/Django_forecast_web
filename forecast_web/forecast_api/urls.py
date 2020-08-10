from .views import ForecastView
from django.urls import path

urlpatterns = [
    path('forecast/', ForecastView.as_view(), name="Forecast"),
]
