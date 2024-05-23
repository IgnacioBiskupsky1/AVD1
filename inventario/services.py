
from decimal import Decimal
from django.db import transaction
from .models import CompProducto, StockAditivo, StockProductos

def producir_producto(producto_id, cantidad_producir):
    # Convertir cantidad_producir a Decimal
    cantidad_producir = Decimal(cantidad_producir)

    with transaction.atomic():
        # Obtener todos los componentes del producto
        
        componentes = CompProducto.objects.filter(productos_id=producto_id)

        # Verificar si hay suficientes aditivos en stock
        for componente in componentes:
            stock_aditivo = StockAditivo.objects.get(nomAditivo=componente.info_aditivo)
            cantidad_necesaria = cantidad_producir * componente.vv #* componente.pp  

            if stock_aditivo.stock_ad_cant < cantidad_necesaria:
                raise ValueError(f"No hay suficiente stock del aditivo {componente.info_aditivo.adtv_nom}.")
            else:
                stock_aditivo.stock_ad_cant -= cantidad_necesaria
                stock_aditivo.save()
                
        # Consumir el stock de aditivos
        #for componente in componentes:
        #    stock_aditivo = StockAditivo.objects.get(nomAditivo=componente.info_aditivo)
        #    cantidad_necesaria = componente.pp * cantidad_producir * componente.vv
        #    stock_aditivo.stock_ad_cant -= cantidad_necesaria
        #    stock_aditivo.save()

        # Incrementar el stock del producto
        stock_productos, created = StockProductos.objects.get_or_create(
            productos=producto_id,
            defaults={'stock_prod_cant': cantidad_producir}
        )
        if not created:
            stock_productos.stock_prod_cant += cantidad_producir
        stock_productos.save()

        return stock_productos
