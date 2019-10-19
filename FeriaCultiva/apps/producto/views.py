from django.shortcuts import render
from apps.producto.models import Producto

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class AgregarProducto(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Producto
	template_name = 'Producto/agregarProducto.html'
	success_url = reverse_lazy('producto:listar')
	fields = '__all__'

class ListarProductos(LoginRequiredMixin,ListView):
	model = Producto
	template_name = 'Producto/listarProductos.html'

class DetalleProducto(LoginRequiredMixin,DetailView):
	model = Producto
	template_name = 'Producto/detalleProducto.html'

class ModificarProducto(LoginRequiredMixin,UpdateView):
	model = Producto
	template_name = 'Producto/agregarProducto.html'
	success_url = reverse_lazy('productos:listar')
	fields = '__all__'

class EliminarProducto(LoginRequiredMixin,DeleteView):
	model = Producto
	template_name = 'Producto/eliminarProducto.html'
	success_url = reverse_lazy('productos:listar')
'''
class ListarProductosPorRubro(LoginRequiredMixin, ListView):

	template_name = 'Productos/listarProductos.html'

	def get_queryset(self):
		onlyDisp = self.request.GET.get('disponibles')
		desde = self.request.GET.get('desde', None)
		hasta = self.request.GET.get('hasta', None)
		rubro = self.request.GET.get('filtro', None)

		if not rubro:
			rubro = "0"
		
		if not desde:
			desde = 0
		if not hasta:
			hasta = 9999999999

		if rubro == "0":
			if onlyDisp == "si":
				x = Productos.objects.filter(stock__gt = 0, precio__gte = desde, precio__lte = hasta)
			else:
				x = Productos.objects.filter(precio__gte = desde, precio__lte = hasta)
		else:
			if onlyDisp == "si":
				x = Productos.objects.filter(rubro = rubro, stock__gt = 0, precio__gte = desde, precio__lte = hasta)
			else:
				x = Productos.objects.filter(rubro = rubro, precio__gte = desde, precio__lte = hasta)	
		return x

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubros'] = Rubro.objects.all()

		favorites = Favorite.objects.filter(user = self.request.user).values('producto')

		fav = []
		for p in context['object_list']:
			for i in favorites:
				if p.pk == i['producto']:
					fav.append(p.pk)

		context['favList'] = fav
		
		rubro = self.request.GET.get('filtro', None)
		if not rubro:
			rubro = "0"
		print("Rubro: ", rubro)
		if rubro == "0":
			context['rubroUnico'] = "Todos"
		else:
			context['rubroUnico'] = Rubro.objects.get(id = rubro).nombre
		return context
'''