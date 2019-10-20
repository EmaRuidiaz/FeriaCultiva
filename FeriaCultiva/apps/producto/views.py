from django.shortcuts import render
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from .models import Producto

class ListarProductos(ListView):
    model = Producto
    template_name = 'producto/listar.html'


# def ListarProductos(request):
#     context = {}
#     context['object_list'] = Producto.objects.all()

#     paginator = Paginator(context,2)
#     page = request.GET.get('page')
#     context = paginator.get_page(page)
#     return render(request, 'producto/listar.html', {'context' : context})