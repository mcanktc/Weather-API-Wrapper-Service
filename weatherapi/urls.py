from django.urls import path
from . import views

urlpatterns = [

path('', views.WeatherApiView.as_view(), name='weatherapi'),

]