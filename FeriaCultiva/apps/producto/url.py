from django.contrib import admin
from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('Detalle/<int:pk>', views.DetalleProducto.as_view(), name='Detalle'),  
]
