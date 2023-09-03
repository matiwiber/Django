from pyexpat.errors import messages
from typing import Optional, Type
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'miapp/login.html'
    success_url = reverse_lazy('')

class PaginaPrincipalView(View):
    def get(self, request):
        return render(request, 'miapp/pagina_principal.html')

class BuscarView(ListView):
    template_name = 'miapp/buscar.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Producto.objects.filter(nombre__icontains=query)
        return Producto.objects.all()

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

    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       # Modifica el campo de categoría para mostrar el nombre en lugar del ID
       form.fields['categoria'].queryset = Categoria.objects.all()
       return form

# Vistas de funciones
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'¡Registro exitoso! Ahora puedes iniciar sesión como {username}.')
            return redirect('/login/') 
    else:
        form = UserCreationForm()
    return render(request, 'miapp/register.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('producto-list')

def eliminar_categoria(request, categoria_id):
    # Obtén la categoría que deseas eliminar
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        # Verifica si el usuario confirma la eliminación
        if 'confirmar' in request.POST:
            categoria.delete()
            return redirect('categoria-list')  # Redirige a la lista de categorías después de eliminar una
        else:
            return redirect('categoria-list')  # Redirige de vuelta a la lista sin eliminar

    return render(request, 'miapp/eliminar_categoria.html', {'categoria': categoria})