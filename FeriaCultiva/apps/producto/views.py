from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Producto

class DetalleProducto(DetailView):
    model = Producto
    template_name = 'producto/detalle_producto.html'