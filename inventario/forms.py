#"""
from django import forms
from .models import InfoAditivo, Producto, CompProducto, StockAditivo, Insumo, ProdCopec, StockInsumo, StockProducto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['insumo_nom', 'insumo_vol', 'insumo_env_por_caja', 'insumo_cajas_por_pallet', 'insumo_desc']
        labels = {
            'insumo_nom': 'Nombre de insumo',            
            'insumo_vol': 'Volumen en Litros',
            'insumo_env_por_caja': 'Cantidad de envases por caja',
            'insumo_cajas_por_pallet': 'Cantidad de cajas por pallet',
            'insumo_desc': 'Descripción'
        }

class InfoAditivoForm(forms.ModelForm):
    class Meta:
        model = InfoAditivo
        fields = ['adtv_nom','adtv_dens']  
        labels = {
            'adtv_nom': 'Nombre de la materia prima',
            'adtv_dens': 'Densidad',            
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['producto_nom']
        labels = {
            'producto_nom': 'Nombre del Producto',           
        }
    
class CompProductoForm(forms.ModelForm):
    class Meta:
        model = CompProducto
        fields = ['producto', 'info_aditivo', 'pp', 'vv']
        labels = {
            'producto': 'Nombre del Producto',
            'info_aditivo': 'Nombre del Aditivo', 
            'pp': 'Porcentaje Peso Peso', 
            'vv': 'Porcentaje Volumen Volumen'
        }

class ProdCopecForm(forms.ModelForm):
    class Meta:
        model = ProdCopec
        fields = ['prod_copec_cod','prod_copec_nom','producto', 'insumo']
        labels = {
            'prod_copec_cod':'Codigo de producto COPEC',
            'prod_copec_nom':'Nombre de producto COPEC',
            'producto': 'Nombre del Producto',
            'insumo': 'Nombre del Insumo'
        }

class StockAditivoForm(forms.ModelForm):
    class Meta:
        model = StockAditivo
        fields = ['nomAditivo', 'stock_ad_cant_lt']
        labels = {
            'nomAditivo': 'Nombre del Aditivo',
            'stock_ad_cant_lt': 'Cantidad del Aditivo'  
        }

class StockProductoForm(forms.ModelForm):
    class Meta:
        model = StockProducto
        fields = ['prod_copec', 'stock_prod_cant_vol','stock_prod_cant_uni']
        labels = {            
            'prod_copec': 'Nombre del producto COPEC',
            'stock_prod_cant_vol': 'Cantidad de litros de Producto',
            'stock_prod_cant_uni': 'Cantidad de unidades de Producto'  
        }

class StockInsumoForm(forms.ModelForm):
    class Meta:
        model = StockInsumo
        fields = ['insumo', 'stock_in_cant_unit']
        labels = {            
            'insumo': 'Nombre del Insumo',
            'stock_in_cant_unit': 'Cantidad del Insumo'  
        }

#"""

    
