from django.contrib import admin
from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('producto/', views.ListarProductos.as_view(), name = "ListarProducto"),
]