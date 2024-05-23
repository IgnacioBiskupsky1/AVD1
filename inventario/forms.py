from django import forms
from .models import InfoAditivo, Insumo, Productos, CompProducto, StockAditivo, StockProductos
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

class StockAditivoForm(forms.ModelForm):
    class Meta:
        model = StockAditivo
        fields = ['nomAditivo', 'stock_ad_cant']
        labels = {
            'nomAditivo': 'Nombre del Aditivo',
            'stock_ad_cant': 'Cantidad del Aditivo'  
        }

class StockProductosForm(forms.ModelForm):
    class Meta:
        model = StockProductos
        fields = ['productos', 'stock_prod_cant']
        labels = {            
            'productos': 'Nombre del producto',
            'stock_prod_cant': 'Cantidad del Producto'  
        }

#class StockProductoForm(forms.ModelForm):
#    class Meta:
#        model = StockProducto
#        fields = ['stock_producto_id', 'stock_prod_cant']
#        labels = {            
#            'stock_producto_id': 'Id del stock de producto',
#            'stock_prod_cant': 'Cantidad del Producto'  
#        }