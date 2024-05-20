from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Glicol(models.Model):
    glicol_rang_id = models.AutoField(primary_key=True)
    min_glicol = models.IntegerField()
    max_glicol = models.IntegerField()

class InfoAditivo(models.Model):
    adtv_id = models.AutoField(primary_key=True)
    adtv_nom = models.CharField(max_length=60, blank=True, null=True)
    adtv_dens = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.name

class Mezcla(models.Model):
    mezcla_id = models.AutoField(primary_key=True)
    info_aditivo = models.ForeignKey(InfoAditivo, on_delete=models.CASCADE)
    pp = models.DecimalField(max_digits=5, decimal_places=2)
    vv = models.DecimalField(max_digits=5, decimal_places=2)

class Olor(models.Model):
    olor_id = models.AutoField(primary_key=True)
    olor_nombre = models.CharField(max_length=10)

class Ph(models.Model):
    id_rang_ph = models.AutoField(primary_key=True)
    ph_min = models.DecimalField(max_digits=3, decimal_places=1)
    ph_max = models.DecimalField(max_digits=3, decimal_places=1)

class Producto(models.Model):
    prod_id = models.AutoField(primary_key=True)
    mezcla = models.ForeignKey(Mezcla, on_delete=models.CASCADE)
    prod_nom = models.CharField(max_length=50)
    prod_ph = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    ph = models.ForeignKey(Ph, on_delete=models.SET_NULL, null=True, blank=True)
    apariencia = models.ForeignKey('Apariencia', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    olor = models.ForeignKey(Olor, on_delete=models.CASCADE)
    prod_glicol = models.IntegerField(null=True, blank=True)
    glicol_rang = models.ForeignKey(Glicol, on_delete=models.SET_NULL, null=True, blank=True)
    prod_fp = models.IntegerField(null=True, blank=True)
    prod_grav_esp = models.DecimalField(max_digits=5, decimal_places=5, null=True, blank=True)
    prod_api = models.CharField(max_length=50, blank=True, null=True)
    prod_tk_agua = models.IntegerField(null=True, blank=True)
    prod_tk_prod = models.IntegerField(null=True, blank=True)

# Define también los modelos Apariencia y Color si tienes los detalles.
class Apariencia(models.Model):
    id_apar = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    
#Modelo de Insumos
class Insumo(models.Model):
    insumo_id = models.AutoField(primary_key=True)
    in_nombre = models.CharField(max_length=60, blank=True, null=True)
    in_desc = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.name