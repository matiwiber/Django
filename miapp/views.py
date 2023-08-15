from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm


def PaginaPrincipalView(request):
    return render(request, 'miapp/pagina_principal.html')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'miapp/categoria_list.html'

class ProductoListView(ListView):
    model = Producto
    template_name = 'miapp/producto_list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'miapp/categoria_form.html'
    success_url = reverse_lazy('categoria-list')

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'miapp/producto_form.html'
    success_url = reverse_lazy('producto-list')

class BuscarView(ListView):
    template_name = 'miapp/buscar.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Producto.objects.filter(nombre__icontains=query)
        return Producto.objects.all()
