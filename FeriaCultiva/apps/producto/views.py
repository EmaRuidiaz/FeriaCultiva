from django.shortcuts import render
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from .models import Producto

class ListarProductos(ListView):
    model = Producto
    paginate_by = 12
    template_name = 'producto/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print (context)
        print('context')
        paginator = context['paginator']
        page_numbers_range = 10 #Cantidad de página que se va a mostrar 
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        print (self.request)
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


# class BookListView(ListView):
#     model=Book
#     paginate_by=10
#     template_name='book/book_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print (context)
#         paginator = context['paginator']
#         page_numbers_range = 10  # Display 5 page numbers
#         max_index = len(paginator.page_range)

#         page = self.request.GET.get('page')
#         print (self.request)
#         current_page = int(page) if page else 1

#         start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#         end_index = start_index + page_numbers_range
#         if end_index >= max_index:
#             end_index = max_index

#         page_range = paginator.page_range[start_index:end_index]
#         context['page_range'] = page_range
#         return context

# book_list = BookListView.as_view()