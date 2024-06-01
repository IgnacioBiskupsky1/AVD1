#"""
import os
from django.conf import settings
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm, InfoAditivoForm, ProductoForm, CompProductoForm, StockAditivoForm, InsumoForm, StockProductoForm, StockInsumoForm, ProdCopecForm, OdpForm, CalidadForm
from .models import InfoAditivo, Producto, CompProducto, StockAditivo, Insumo, StockProducto, StockInsumo, ProdCopec, LoteProd
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from .utils import link_callback
from decimal import Decimal
from django.db import transaction
import math

# Create your views here.
##################################### METODOS USUARIO #####################################
def user_list(request):
    users = User.objects.all ()
    return render(request, 'usercrud/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'usercrud/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usercrud:user_list')
    else:
        form = UserForm()
    return render(request, 'usercrud/user_create.html', {'form': form})
    
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('usercrud:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'usercrud/user_form.html', {'form': form})    
    
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('usercrud:user_list')
    return render(request, 'usercrud/user_delete.html', {'user': user})

def login_user(request):
    context={}
    return render(request, 'usercrud/login_user.html', context)

def edituser(request):
    context={}
    return render(request, 'usercrud/edituser.html', context) 

##################################### PLANTILLA BASE #####################################

def welcome_user(request):
    return render(request, 'usercrud/welcome_user.html') 

def home(request):
    context={}
    return render(request, 'user/home.html', context)

##################################### METODOS MATERIA PRIMA #####################################

def crud_mp(request):
    mps = InfoAditivo.objects.all()
    return render(request, 'inventary/materia_prima/crud_mp.html', {'mps': mps})

def ingresar_mp(request):
    if request.method == 'POST':
        form = InfoAditivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_mp')  
    else:
        form = InfoAditivoForm()
    return render(request, 'inventary/materia_prima/ingresar_mp.html', {'form': form})

def editar_mp(request, adtv_id):
    aditivo = get_object_or_404(InfoAditivo, adtv_id=adtv_id)
    if request.method == 'POST':
        form = InfoAditivoForm(request.POST, instance=aditivo)
        if form.is_valid():
            form.save()
            return redirect('/crud_mp')  # Cambia 'listar_aditivos' por el nombre de tu vista de listado de aditivos
    else:
        form = InfoAditivoForm(instance=aditivo)
    return render(request, 'inventary/materia_prima/editar_mp.html', {'form': form})

def eliminar_mp(request, adtv_id):
    aditivo = get_object_or_404(InfoAditivo, adtv_id=adtv_id)
    if request.method == 'POST':
        aditivo.delete()
        return redirect('/crud_mp')  # Redirigir a la página de listado de productos
    return render(request, 'inventary/materia_prima/eliminar_mp.html', {'aditivo': aditivo})

def listar_mp(request):
    mps = InfoAditivo.objects.all()
    return render(request, 'inventary/materia_prima/listar_mp.html', {'mps': mps}) 

##################################### METODOS INSUMO #####################################

def crud_insu(request):
    insus = Insumo.objects.all()
    return render(request, 'inventary/insumos/crud_insu.html', {'insus': insus}) 

def listar_in(request):
    insus = Insumo.objects.all()
    return render(request, 'inventary/insumos/listar_insumo.html', {'insus': insus})

def ingresar_in(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_insu')  # Cambia 'home' por el nombre de tu URL de inicio
    else:
        form = InsumoForm()
    return render(request, 'inventary/insumos/ingresar_insumo.html', {'form': form})

def eliminar_in(request, insumo_id):
    insumo = get_object_or_404(Insumo, insumo_id=insumo_id)
    if request.method == 'POST':
        insumo.delete()
        return redirect('/crud_insu')  # Redirigir a la página de listado de productos
    return render(request, 'inventary/insumos/eliminar_insumo.html', {'insumo': insumo})

def editar_in(request, insumo_id):
    insumo = get_object_or_404(Insumo, insumo_id=insumo_id)
    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('/crud_insu')  
    else:
        form = InsumoForm(instance=insumo)
    return render(request, 'inventary/insumos/editar_insumo.html', {'form': form})

##################################### METODOS PRODUCTO #####################################

def crud_producto(request):
    productos = Producto.objects.all()
    return render(request, 'inventary/productos/crud_producto.html', {'productos': productos}) 

def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_comp')  # Cambia 'home' por el nombre de tu URL de inicio
    else:
        form = ProductoForm()
    return render(request,'inventary/productos/ingresar_producto.html', {'form': form})

def editar_producto(request, productos_id):
    producto = get_object_or_404(Producto, productos_id=productos_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto')  
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventary/productos/editar_producto.html', {'form': form})

def eliminar_producto(request, productos_id):
    producto = get_object_or_404(Producto, productos_id=productos_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/crud_producto')  # Redirigir a la página de listado de productos
    return render(request, 'inventary/productos/eliminar_producto.html', {'producto': producto})

##################################### METODOS PRODUCTO COPEC #####################################

def crud_producto_copec(request):
    productos = ProdCopec.objects.all()
    return render(request, 'inventary/prod_copec/crud_producto_copec.html', {'productos': productos}) 

def ingresar_producto_copec(request):
    if request.method == 'POST':
        form = ProdCopecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto_copec')  
    else:
        form = ProdCopecForm()
    return render(request,'inventary/prod_copec/ingresar_producto_copec.html', {'form': form})

def editar_producto_copec(request, prod_copec_id):
    producto = get_object_or_404(ProdCopec, prod_copec_id=prod_copec_id)
    if request.method == 'POST':
        form = ProdCopecForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto_copec')  
    else:
        form = ProdCopecForm(instance=producto)
    return render(request, 'inventary/prod_copec/editar_producto_copec.html', {'form': form})

def eliminar_producto_copec(request, prod_copec_id):
    producto = get_object_or_404(ProdCopec, prod_copec_id=prod_copec_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/crud_producto_copec')  
    return render(request, 'inventary/prod_copec/eliminar_producto_copec.html', {'producto': producto})

##################################### METODOS COMPOSICION #####################################

def crud_comp(request):
    
    producto_seleccionado = request.GET.get('producto', None)
    
    if producto_seleccionado:
        comps = CompProducto.objects.filter(producto__producto_nom = producto_seleccionado)
    else:
        comps = CompProducto.objects.none
    
    productos = CompProducto.objects.values_list('producto__producto_nom', flat=True).distinct()
    
    return render(request, 'inventary/comp_producto/crud_comp.html', {'comps': comps, 'productos': productos, 'producto_seleccionado': producto_seleccionado},) 


def ingresar_comp(request):
    if request.method == 'POST':
        form = CompProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_comp')  # Cambia 'home' por el nombre de tu URL de inicio
    else:
        form = CompProductoForm()
    return render(request, 'inventary/comp_producto/ingresar_comp.html', {'form': form})

def editar_comp(request, comp_producto_id):
    composicion = get_object_or_404(CompProducto, comp_producto_id=comp_producto_id)
    if request.method == 'POST':
        form = CompProductoForm(request.POST, instance=composicion)
        if form.is_valid():
            form.save()
            return redirect('/crud_comp')  
    else:
        form = CompProductoForm(instance=composicion)
    return render(request, 'inventary/comp_producto/editar_comp.html', {'form': form})

def eliminar_comp(request, comp_producto_id):
    composicion = get_object_or_404(CompProducto, comp_producto_id=comp_producto_id)
    if request.method == 'POST':
        composicion.delete()
        return redirect('/crud_comp')  # Redirigir a la página de listado de productos
    return render(request, 'inventary/comp_producto/eliminar_comp.html', {'composicion': composicion})


##################################### METODOS STOCK MP #####################################

def crud_stock_mp(request):
    stockmps = StockAditivo.objects.all()
    return render(request, 'inventary/stock_mp/crud_stock_mp.html', {'stockmps': stockmps}) 

def ingresar_stock_mp(request):
    if request.method == 'POST':
        form = StockAditivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_mp') 
    else:
        form = StockAditivoForm()
    return render(request, 'inventary/stock_mp/ingresar_stock_mp.html', {'form': form})

def editar_stock_mp(request, stock_ad_id):
    stockmp = get_object_or_404(StockAditivo, stock_ad_id=stock_ad_id)
    if request.method == 'POST':
        form = StockAditivoForm(request.POST, instance=stockmp)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_mp')  
    else:
        form = StockAditivoForm(instance=stockmp)
    return render(request, 'inventary/stock_mp/editar_stock_mp.html', {'form': form})

##################################### METODOS STOCK PRODUCTOS #####################################

def crud_stock_prod(request):
    stockprods = StockProducto.objects.all()
    return render(request, 'inventary/stock_producto/crud_stock_prod.html', {'stockprods': stockprods}) 

def ingresar_stock_prod(request):
    if request.method == 'POST':
        form = StockProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_prod')  
    else:
        form = StockProductoForm()
    return render(request, 'inventary/stock_producto/ingresar_stock_prod.html', {'form': form})

def editar_stock_prod(request, stock_producto_id):
    stockprod = get_object_or_404(StockProducto, stock_producto_id=stock_producto_id)
    if request.method == 'POST':
        form = StockProductoForm(request.POST, instance=stockprod)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_prod')  
    else:
        form = StockProductoForm(instance=stockprod)
    return render(request, 'inventary/stock_producto/editar_stock_prod.html', {'form': form})

##################################### METODOS STOCK INSUMO #####################################

def crud_stock_insumo(request):
    stockinsus = StockInsumo.objects.all()
    return render(request, 'inventary/stock_insumo/crud_stock_insumo.html', {'stockinsus': stockinsus}) 

def ingresar_stock_insumo(request):
    if request.method == 'POST':
        form = StockInsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_insumo') 
    else:
        form = StockInsumoForm()
    return render(request, 'inventary/stock_insumo/ingresar_stock_insumo.html', {'form': form})

def editar_stock_insumo(request, stock_in_id):
    stockinsu = get_object_or_404(StockInsumo, stock_in_id=stock_in_id)
    if request.method == 'POST':
        form = StockInsumoForm(request.POST, instance=stockinsu)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_insumo')  
    else:
        form = StockInsumoForm(instance=stockinsu)
    return render(request, 'inventary/stock_insumo/editar_stock_insumo.html', {'form': form})

##################################### TRANSACCION COPEC DIRECTA CON EL PRODUCTO#####################################

@transaction.atomic
def orden_de_prod(request):

    if request.method == 'POST':
        prod_copec_id  = request.POST.get('prod_copec_id')
        valor_total = request.POST.get('valor_total')

        try:
            valor_total = Decimal(valor_total)
            agregar_stock(prod_copec_id,valor_total)
            HttpResponse("Stock agregado exitosamente")
            return redirect('/crud_stock_prod')
        except ValueError as e:
            return HttpResponse(f"Error: {e}")
    else:
        prod_copecs = ProdCopec.objects.all()

    return render(request, 'ventanas_prod/orden_de_produccion.html', {
        'prod_copecs': prod_copecs,
    })

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

###################################################################################################################

def cruds(request):
    return render(request, 'cruds.html',{})

########################################## METODOS ORDEN PRODUCCION ################################################

def crud_orden_prod(request):
    odps = LoteProd.objects.all()
    return render(request, 'ventanas_prod/orden_prod/crud_orden_prod.html', {'odps': odps}) 

def ingresar_orden_prod(request):
    if request.method == 'POST':
        form = OdpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_orden_prod') 
    else:
        form = OdpForm()
    return render(request, 'ventanas_prod/orden_prod/ingresar_orden_prod.html', {'form': form})

def editar_orden_prod(request, lote_prod_id):
    odp = get_object_or_404(LoteProd, lote_prod_id=lote_prod_id)
    if request.method == 'POST':
        form = OdpForm(request.POST, instance=odp)
        if form.is_valid():
            form.save()
            return redirect('/crud_orden_prod')  
    else:
        form = OdpForm(instance=odp)
    return render(request, 'ventanas_prod/orden_prod/editar_orden_prod.html', {'form': form})

########################################## METODOS CALIDAD ################################################

def crud_calidad(request):
    odps = LoteProd.objects.all()
    return render(request, 'ventanas_prod/analisis_calidad/crud_calidad.html', {'odps': odps}) 

def editar_calidad(request, lote_prod_id):
    odp = get_object_or_404(LoteProd, lote_prod_id=lote_prod_id)
    if request.method == 'POST':
        form = CalidadForm(request.POST, instance=odp)
        if form.is_valid():
            form.save()
            return redirect('/crud_orden_prod')
    else:
        form = CalidadForm(instance=odp)
    return render(request, 'ventanas_prod/analisis_calidad/editar_calidad.html', {'form': form})

########################################## METODOS CERTIFICADO ################################################

def crud_certificado(request):
    odps = LoteProd.objects.all()
    return render(request, 'ventanas_prod/despacho/crud_certificado.html', {'odps': odps})

def gen_certificado(request, lote_prod_id):
    # Obtener el objeto correspondiente al lote_prod_id
    odp = get_object_or_404(LoteProd, lote_prod_id=lote_prod_id)
    return render(request, 'ventanas_prod/despacho/gen_certificado.html', {'odp': odp}) 

"""    
    # Renderizar el HTML a una cadena
    html = render_to_string('ventanas_prod/despacho/gen_certificado.html', {'odp': odp})

    # Crear una respuesta HTTP con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificado_{lote_prod_id}.pdf"'

    # Convertir el HTML a PDF usando xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    # Verificar si hubo algún error
    if pisa_status.err:
        return HttpResponse('Ocurrió un error al generar el PDF', status=500)
    
    return response

"""