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


urlpatterns = [
    path('', views.PaginaPrincipalView, name='pagina-principal'),
    path('/categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('/productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('/categoria/nueva/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('/producto/nuevo/', views.ProductoCreateView.as_view(), name='producto-create'),
    path('/buscar/', views.BuscarView.as_view(), name='buscar'),
]