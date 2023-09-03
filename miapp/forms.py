from django import forms
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modifica el campo de categoría para mostrar el nombre en lugar del ID
        self.fields['categoria'].queryset = Categoria.objects.all()