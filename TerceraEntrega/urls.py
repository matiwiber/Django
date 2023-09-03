"""
URL configuration for TerceraEntrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp.models import *
from miapp import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.PaginaPrincipalView.as_view(), name='pagina-principal'),
    path('categorias/', login_required(views.CategoriaListView.as_view()), name='categoria-list'),
    path('productos/', login_required(views.ProductoListView.as_view()), name='producto-list'),
    path('categoria/nueva/', login_required(views.CategoriaCreateView.as_view()), name='categoria-create'),
    path('producto/nuevo/', login_required(views.ProductoCreateView.as_view()), name='producto-create'),
    path('producto/<int:producto_id>/eliminar/', login_required(views.eliminar_producto), name='eliminar-producto'),
    path('buscar/', views.BuscarView.as_view(), name='buscar'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]