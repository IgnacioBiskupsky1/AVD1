from django.conf import settings
from django.contrib.staticfiles import finders
import os
from .models import ProdCopec, StockAditivo, StockInsumo, StockProducto, CompProducto
from decimal import Decimal
from django.db import transaction
import math

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = finders.find(uri.replace(settings.STATIC_URL, ""))
        if not path:
            raise Exception('File {} not found in STATICFILES_DIRS.'.format(uri))
    else:
        return uri

    if not os.path.isfile(path):
        raise Exception('Media URI must start with {} or {}'.format(settings.STATIC_URL, settings.MEDIA_URL))

    return path

    ##############################################################################################################

@transaction.atomic
def agregar_stock(prod_copec_id, valor_total):
    try:
        
        prod_copec = ProdCopec.objects.get(prod_copec_id=prod_copec_id)
        insumo = prod_copec.insumo
        stock_producto, created = StockProducto.objects.get_or_create(
            prod_copec=prod_copec,
            defaults={'stock_prod_cant_vol': valor_total,
                      'stock_prod_cant_uni':math.trunc(Decimal(valor_total) / insumo.insumo_vol)}
        )
        
        if not created:                
            stock_producto.stock_prod_cant_vol +=  Decimal(valor_total)
            stock_producto.stock_prod_cant_uni +=  math.trunc(Decimal(valor_total) / insumo.insumo_vol)
            stock_producto.save()

        comp_productos = CompProducto.objects.filter(producto=prod_copec.producto)
        for comp_producto in comp_productos:
            aditivo = comp_producto.info_aditivo
            cantidad_a_descontar = Decimal(valor_total) * comp_producto.vv
            stock_aditivo = StockAditivo.objects.get(nomAditivo=aditivo)
            if stock_aditivo.stock_ad_cant_lt < cantidad_a_descontar:
                raise ValueError(f"No hay suficiente stock del aditivo {aditivo.adtv_nom}")
            stock_aditivo.stock_ad_cant_lt -= cantidad_a_descontar
            stock_aditivo.save()

        cantidad_a_descontar_insumo = math.trunc(Decimal(valor_total) / insumo.insumo_vol)
        stock_insumo = StockInsumo.objects.get(insumo=insumo)
        if stock_insumo.stock_in_cant_unit < cantidad_a_descontar_insumo:
            raise ValueError(f"No hay suficiente stock del insumo {insumo.insumo_nom}")
        stock_insumo.stock_in_cant_unit -= cantidad_a_descontar_insumo
        stock_insumo.save()
        
    except ProdCopec.DoesNotExist:
        raise ValueError(f"Producto con id {prod_copec_id} no existe")
    except StockAditivo.DoesNotExist:
        raise ValueError(f"Stock de aditivo no existe")
    except StockInsumo.DoesNotExist:
        raise ValueError(f"Stock de insumo no existe")