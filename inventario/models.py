from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Modelo de Insumos
class Insumo(models.Model):
    insumo_id = models.AutoField(primary_key=True)
    in_nombre = models.CharField(max_length=60, blank=True, null=True)
    in_desc = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.name

class InfoAditivo(models.Model):
    adtv_id = models.AutoField(primary_key=True)
    adtv_nom = models.CharField(max_length=60, blank=True, null=True)
    adtv_dens = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.adtv_nom

class Productos(models.Model):
    productos_id = models.AutoField(primary_key=True)
    productos_nom = models.CharField(max_length=50)
    def __str__(self):
        return self.productos_nom
    
class CompProducto(models.Model):
    comp_producto_id = models.AutoField(primary_key=True)
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    info_aditivo = models.ForeignKey(InfoAditivo, on_delete=models.CASCADE)
    pp = models.DecimalField(max_digits=5, decimal_places=5)
    vv = models.DecimalField(max_digits=6, decimal_places=5, default=1.00000)
    def __str__(self):
        return self.productos

class StockAditivo(models.Model):
    stock_ad_id = models.AutoField(primary_key=True)
    nomAditivo = models.ForeignKey(InfoAditivo, on_delete=models.CASCADE)
    stock_ad_cant = models.DecimalField(max_digits=10, decimal_places=2)

class StockProductos(models.Model):
    stock_producto_id = models.AutoField(primary_key=True)
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    stock_prod_cant = models.DecimalField(max_digits=10, decimal_places=2)



###################################### ESTO NO SIRVE (...POR AHORA) #############################################

#class StockProducto(models.Model):
#    stock_producto_id = models.AutoField(primary_key=True)
#    comp_producto = models.ForeignKey(CompProducto, on_delete=models.CASCADE)
#    stock_prod_cant = models.DecimalField(max_digits=10, decimal_places=2)#

#    def __str__(self):
#        return f'{self.comp_producto.productos.productos_nom} - {self.cantidad}'

#class Mezcla(models.Model):
#    mezcla_id = models.AutoField(primary_key=True)
#    info_aditivo = models.ForeignKey(InfoAditivo, on_delete=models.CASCADE)
#    pp = models.DecimalField(max_digits=5, decimal_places=2)
#    vv = models.DecimalField(max_digits=5, decimal_places=2)

#class Olor(models.Model):
#    olor_id = models.AutoField(primary_key=True)
#    olor_nombre = models.CharField(max_length=10)

#class Ph(models.Model):
#    id_rang_ph = models.AutoField(primary_key=True)
#    ph_min = models.DecimalField(max_digits=3, decimal_places=1)
#    ph_max = models.DecimalField(max_digits=3, decimal_places=1)

# Define también los modelos Apariencia y Color si tienes los detalles.
#class Apariencia(models.Model):
#    id_apar = models.AutoField(primary_key=True)
#    descripcion = models.CharField(max_length=100)

#class Color(models.Model):
#    id_color = models.AutoField(primary_key=True)
#    descripcion = models.CharField(max_length=100)

#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)

#class Glicol(models.Model):
#    glicol_rang_id = models.AutoField(primary_key=True)
#    min_glicol = models.IntegerField()
#    max_glicol = models.IntegerField()

#class Producto(models.Model):
#    prod_id = models.AutoField(primary_key=True)
#    mezcla = models.ForeignKey(Mezcla, on_delete=models.CASCADE)
#    prod_nom = models.CharField(max_length=50)
#    prod_ph = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
#    ph = models.ForeignKey(Ph, on_delete=models.SET_NULL, null=True, blank=True)
#    apariencia = models.ForeignKey('Apariencia', on_delete=models.CASCADE)
#    color = models.ForeignKey('Color', on_delete=models.CASCADE)
#    olor = models.ForeignKey(Olor, on_delete=models.CASCADE)
#    prod_glicol = models.IntegerField(null=True, blank=True)
#    glicol_rang = models.ForeignKey(Glicol, on_delete=models.SET_NULL, null=True, blank=True)
#    prod_fp = models.IntegerField(null=True, blank=True)
#    prod_grav_esp = models.DecimalField(max_digits=5, decimal_places=5, null=True, blank=True)
#    prod_api = models.CharField(max_length=50, blank=True, null=True)
#    prod_tk_agua = models.IntegerField(null=True, blank=True)
#    prod_tk_prod = models.IntegerField(null=True, blank=True)   

   
