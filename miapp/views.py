from pyexpat.errors import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




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
            return redirect('/login/')  # Reemplaza 'home' con la URL a la que deseas redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'miapp/register.html', {'form': form})



class CustomLoginView(LoginView):
    template_name = 'miapp/login.html'  # Nombre de la plantilla de inicio de sesión
    success_url = reverse_lazy('')  # URL a la que se redirigirá después del inicio de sesión


def PaginaPrincipalView(request):
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


