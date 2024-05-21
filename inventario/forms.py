from django import forms
from .models import InfoAditivo, Insumo, Productos, CompProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MpForm(forms.ModelForm):
    class Meta:
        model = InfoAditivo
        fields = ['adtv_id', 'adtv_nom', 'adtv_dens']
        labels = {
            'adtv_nom': 'Nombre de la materia prima',
            'adtv_dens': 'Densidad',            
        }
        
class InForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['insumo_id', 'in_nombre', 'in_desc']
        labels = {
            'in_nombre': 'Nombre de insumo',
            'in_desc': 'Descripción',            
        }

class InfoAditivoForm(forms.ModelForm):
    class Meta:
        model = InfoAditivo
        fields = ['adtv_nom', 'adtv_dens']  # Lista los campos que deseas editar en el formulario


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['productos_nom']
        labels = {
            'productos_nom': 'Nombre del Producto',           
        }

class CompProductoForm(forms.ModelForm):
    class Meta:
        model = CompProducto
        fields = ['productos', 'info_aditivo', 'pp', 'vv']
        labels = {
            'productos': 'Nombre del Producto',
            'info_aditivo': 'Nombre del Aditivo', 
            'pp': 'Porcentaje Peso Peso', 
            'vv': 'Porcentaje Volumen Volumen'
        }