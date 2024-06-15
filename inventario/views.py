#"""
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserForm, InfoAditivoForm, ProductoForm, CompProductoForm, StockAditivoForm, InsumoForm, StockProductoForm, StockInsumoForm, ProdCopecForm, OdpForm, CalidadForm, GuiaDespachoForm
from .models import InfoAditivo, Producto, CompProducto, StockAditivo, Insumo, StockProducto, StockInsumo, ProdCopec, LoteProd, Despacho
from django.http import HttpResponse
from django.middleware.csrf import get_token
from .utils import link_callback, agregar_stock, generar_despacho, aumentar_stock_mp, aumentar_stock_insumo, actualizar_despacho, despachar
from django.http import HttpResponseForbidden
from decimal import Decimal
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .decorators import allowed_users


# Create your views here.
##################################### METODOS USUARIO #####################################
@login_required(login_url='login')
def crud_usuario(request):
    users = User.objects.all ()
    return render(request, 'usercrud/crud_usuario.html', {'users': users})

@login_required(login_url='login')
def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_usuario')
    else:
        form = UserForm()
    return render(request, 'usercrud/crear_usuario.html', {'form': form})

@login_required(login_url='login') 
def editar_usuario(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/crud_usuario')
    else:
        form = UserForm(instance=user)
    return render(request, 'usercrud/editar_usuario.html', {'form': form})    

@login_required(login_url='login')
def eliminar_usuario(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('/crud_usuario')
    return render(request, 'usercrud/eliminar_usuario.html', {'user': user})


##################################### METODOS LOGIN LOGOUT #####################################

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                messages.info(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
            
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

##################################### PLANTILLA BASE #####################################

@login_required(login_url='login')
#@allowed_users(allowed_roles=['GESTION'])
def home(request):    
    context = {
        'username': request.user.username,
        'grupo': request.user.groups.first()
    }
    return render(request, 'usercrud/welcome_user.html', context)

##################################### METODOS MATERIA PRIMA #####################################

@login_required(login_url='login')
def crud_mp(request):
    
    context = {
            'mps': InfoAditivo.objects.all(),
            'grupo': request.user.groups.first()
        }
    
    return render(request, 'inventary/materia_prima/crud_mp.html', context)

@login_required(login_url='login')
def ingresar_mp(request):
    if request.method == 'POST':
        form = InfoAditivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_mp')  
    else:
        form = InfoAditivoForm()
    return render(request, 'inventary/materia_prima/ingresar_mp.html', {'form': form})

@login_required(login_url='login')
def editar_mp(request, adtv_id):
    aditivo = get_object_or_404(InfoAditivo, adtv_id=adtv_id)
    if request.method == 'POST':
        form = InfoAditivoForm(request.POST, instance=aditivo)
        if form.is_valid():
            form.save()
            return redirect('/crud_mp')
    else:
        form = InfoAditivoForm(instance=aditivo)
    return render(request, 'inventary/materia_prima/editar_mp.html', {'form': form})

@login_required(login_url='login')
def eliminar_mp(request, adtv_id):
    aditivo = get_object_or_404(InfoAditivo, adtv_id=adtv_id)
    if request.method == 'POST':
        aditivo.delete()
        return redirect('/crud_mp')  
    return render(request, 'inventary/materia_prima/eliminar_mp.html', {'aditivo': aditivo})

@login_required(login_url='login')
def listar_mp(request):
    mps = InfoAditivo.objects.all()
    return render(request, 'inventary/materia_prima/listar_mp.html', {'mps': mps}) 

##################################### METODOS INSUMO #####################################
@login_required(login_url='login')
def crud_insu(request):
    insus = Insumo.objects.all()
    return render(request, 'inventary/insumos/crud_insu.html', {'insus': insus}) 

@login_required(login_url='login')
def listar_in(request):
    insus = Insumo.objects.all()
    return render(request, 'inventary/insumos/listar_insumo.html', {'insus': insus})

@login_required(login_url='login')
def ingresar_in(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_insu')
    else:
        form = InsumoForm()
    return render(request, 'inventary/insumos/ingresar_insumo.html', {'form': form})

@login_required(login_url='login')
def eliminar_in(request, insumo_id):
    insumo = get_object_or_404(Insumo, insumo_id=insumo_id)
    if request.method == 'POST':
        insumo.delete()
        return redirect('/crud_insu')  
    return render(request, 'inventary/insumos/eliminar_insumo.html', {'insumo': insumo})

@login_required(login_url='login')
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
@login_required(login_url='login')
def crud_producto(request):
    productos = Producto.objects.all()
    return render(request, 'inventary/productos/crud_producto.html', {'productos': productos}) 

@login_required(login_url='login')
def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_comp')  
    else:
        form = ProductoForm()
    return render(request,'inventary/productos/ingresar_producto.html', {'form': form})

@login_required(login_url='login')
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, producto_id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto')  
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventary/productos/editar_producto.html', {'form': form})

@login_required(login_url='login')
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, producto_id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/crud_producto')
    return render(request, 'inventary/productos/eliminar_producto.html', {'producto': producto})

##################################### METODOS PRODUCTO COPEC #####################################
@login_required(login_url='login')
def crud_producto_copec(request):
    productos = ProdCopec.objects.all()
    return render(request, 'inventary/prod_copec/crud_producto_copec.html', {'productos': productos}) 

@login_required(login_url='login')
def ingresar_producto_copec(request):
    if request.method == 'POST':
        form = ProdCopecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto_copec')  
    else:
        form = ProdCopecForm()
    return render(request,'inventary/prod_copec/ingresar_producto_copec.html', {'form': form})

@login_required(login_url='login')
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

@login_required(login_url='login')
def eliminar_producto_copec(request, prod_copec_id):
    producto = get_object_or_404(ProdCopec, prod_copec_id=prod_copec_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/crud_producto_copec')  
    return render(request, 'inventary/prod_copec/eliminar_producto_copec.html', {'producto': producto})

##################################### METODOS COMPOSICION #####################################
@login_required(login_url='login')
def crud_comp(request):
    
    producto_seleccionado = request.GET.get('producto', None)
    
    if producto_seleccionado:
        comps = CompProducto.objects.filter(producto__producto_nom = producto_seleccionado)
    else:
        comps = CompProducto.objects.none
    
    productos = CompProducto.objects.values_list('producto__producto_nom', flat=True).distinct()
    
    return render(request, 
                  'inventary/comp_producto/crud_comp.html',
                  {'comps': comps, 'productos': productos,
                   'producto_seleccionado': producto_seleccionado
                   }) 

@login_required(login_url='login')
def ingresar_comp(request):
    if request.method == 'POST':
        form = CompProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_comp')  
    else:
        form = CompProductoForm()
    return render(request, 'inventary/comp_producto/ingresar_comp.html', {'form': form})

@login_required(login_url='login')
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

@login_required(login_url='login')
def eliminar_comp(request, comp_producto_id):
    composicion = get_object_or_404(CompProducto, comp_producto_id=comp_producto_id)
    if request.method == 'POST':
        composicion.delete()
        return redirect('/crud_comp')
    return render(request, 'inventary/comp_producto/eliminar_comp.html', {'composicion': composicion})


##################################### METODOS STOCK MP #####################################
@permission_required('inventario.can_access_crud_stock_mp', raise_exception=True)
@login_required(login_url='login')
def crud_stock_mp(request):
    context = {
        'username': request.user.username,
        'grupo': request.user.groups.first(),
        'stockmps': StockAditivo.objects.all()
    }
    return render(request, 'inventary/stock_mp/crud_stock_mp.html', context) 

@login_required(login_url='login')
def ingresar_stock_mp(request):
    if request.method == 'POST':
        form = StockAditivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_mp') 
    else:
        form = StockAditivoForm()
    return render(request, 'inventary/stock_mp/ingresar_stock_mp.html', {'form': form})

@login_required(login_url='login')
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

def agregar_stock_mp(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad_mp')
        stock_ad_id = request.POST.get('stock_ad_id')
        
        if not cantidad or not stock_ad_id:
            return HttpResponse('Parámetros incompletos', status=400)    
        
        try:
            cantidad = Decimal(cantidad)
            stock_ad_id = int(stock_ad_id)
            aumentar_stock_mp(stock_ad_id, cantidad)
            return redirect('/crud_stock_mp')
        except ValueError as e:            
            return HttpResponse(str(e), status=400)
    
    return HttpResponse('Método no permitido', status=405)

##################################### METODOS STOCK PRODUCTOS #####################################
@login_required(login_url='login')
def crud_stock_prod(request):
    stockprods = StockProducto.objects.all()
    return render(request, 'inventary/stock_producto/crud_stock_prod.html', {'stockprods': stockprods}) 

@login_required(login_url='login')
def ingresar_stock_prod(request):
    if request.method == 'POST':
        form = StockProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_prod')  
    else:
        form = StockProductoForm()
    return render(request, 'inventary/stock_producto/ingresar_stock_prod.html', {'form': form})

@login_required(login_url='login')
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
@permission_required('inventario.can_access_crud_stock_insumo', raise_exception=True)
@login_required(login_url='login')
def crud_stock_insumo(request):
    context = {
        'username': request.user.username,
        'grupo': request.user.groups.first(),
        'stockinsus': StockInsumo.objects.all()
    }
    return render(request, 'inventary/stock_insumo/crud_stock_insumo.html', context) 

@login_required(login_url='login')
def ingresar_stock_insumo(request):
    if request.method == 'POST':
        form = StockInsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_stock_insumo') 
    else:
        form = StockInsumoForm()
    return render(request, 'inventary/stock_insumo/ingresar_stock_insumo.html', {'form': form})

@login_required(login_url='login')
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

def agregar_stock_insumo(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad_insumo')
        stock_in_id = request.POST.get('stock_in_id')
        
        if not cantidad or not stock_in_id:
            return HttpResponse('Parámetros incompletos', status=400)    
        
        try:
            cantidad = Decimal(cantidad)
            stock_in_id = int(stock_in_id)
            aumentar_stock_insumo(stock_in_id, cantidad)
            return redirect('/crud_stock_insumo')
        except ValueError as e:            
            return HttpResponse(str(e), status=400)
    
    return HttpResponse('Método no permitido', status=405)

###################################################################################################################

@login_required(login_url='login')
@permission_required('inventario.can_access_crud_orden_prod', raise_exception=True)
def cruds(request):
    return render(request, 'cruds.html')

########################################## METODOS ORDEN PRODUCCION ################################################

@login_required(login_url='login')
@permission_required('inventario.can_access_crud_orden_prod', raise_exception=True)
def crud_orden_prod(request):
    
    odps = LoteProd.objects.all()
    return render(request,'ventanas_prod/orden_prod/crud_orden_prod.html',{'odps': odps}) 

@login_required(login_url='login')
def ingresar_orden_prod(request):
    if request.method == 'POST':
        form = OdpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_orden_prod') 
    else:
        form = OdpForm()
    return render(request, 'ventanas_prod/orden_prod/ingresar_orden_prod.html', {'form': form})

@login_required(login_url='login')
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

@login_required(login_url='login')
def eliminar_orden_prod(request, lote_prod_id):
    odp = get_object_or_404(LoteProd, lote_prod_id=lote_prod_id)
    if request.method == 'POST':
        odp.delete()
        return redirect('/crud_orden_prod')
    return render(request, 'ventanas_prod/orden_prod/eliminar_orden_prod.html', {'odp': odp})
########################################## METODOS CALIDAD ################################################

@login_required(login_url='login')
@permission_required('inventario.can_access_crud_calidad', raise_exception=True)
def crud_calidad(request):
    odps = LoteProd.objects.all()

    return render(request,'ventanas_prod/analisis_calidad/crud_calidad.html',{'odps': odps}) 

@login_required(login_url='login')
def editar_calidad(request, lote_prod_id):
    odp = get_object_or_404(LoteProd, lote_prod_id=lote_prod_id)
    if request.method == 'POST':
        form = CalidadForm(request.POST, instance=odp)
        if form.is_valid():
            form.save()
            return redirect('/crud_calidad')
    else:
        form = CalidadForm(instance=odp)
    return render(request, 'ventanas_prod/analisis_calidad/editar_calidad.html', {'form': form})

@login_required(login_url='login')
def confirmar_prod_calidad(request, lote_prod_id):
    odp = get_object_or_404(LoteProd, lote_prod_id=lote_prod_id)

    # Aquí obtén los valores necesarios, por ejemplo:
    prod_copec_id = odp.prod_copec.prod_copec_id
    volumen_odp = odp.volumen_odp    
    # Llama a la función agregar_stock con los parámetros necesarios
    try:
        agregar_stock(prod_copec_id, volumen_odp, lote_prod_id)
        return redirect('/crud_calidad')
    except ValueError as e:
        raise ValueError(e)

########################################## METODOS INVENTARIO BODEGA ################################################
@login_required(login_url='login')
@permission_required('inventario.can_access_crud_despacho', raise_exception=True)
def crud_inv_bodega(request):
    desps = Despacho.objects.all()
    return render(request, 'ventanas_prod/inventario_bodega/crud_inv_bodega.html',{'desps': desps})

########################################## METODOS DESPACHO #########################################################
@login_required(login_url='login')
@permission_required('inventario.can_access_crud_despacho', raise_exception=True)
def crud_despacho(request):
    desps = Despacho.objects.all()        
    return render(request, 'ventanas_prod/despacho_bodega/crud_despacho.html', {'desps': desps}) 

@login_required(login_url='login')
def crud_lote_desp(request):
    odps = LoteProd.objects.all()
    return render(request, 'ventanas_prod/despacho_bodega/crud_lote_desp.html', {'odps': odps})

@login_required(login_url='login')
def ingresar_despacho(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad_despachar')
        lote_id = request.POST.get('lote_id')
        
        if not cantidad or not lote_id:
            return HttpResponse('Parámetros incompletos', status=400)    
        
        try:
            cantidad = Decimal(cantidad)
            lote_id = int(lote_id)
            generar_despacho(lote_id, cantidad)
            return redirect('/crud_despacho')
        except ValueError as e:            
            return HttpResponse(str(e), status=400)
    
    return HttpResponse('Método no permitido', status=405)

@login_required(login_url='login')
def confirmar_despacho(request, despacho_id):
 
    # Llama a la función agregar_stock con los parámetros necesarios
    try:
        despachar(despacho_id)
        return redirect('/crud_despacho')
    except ValueError as e:
        raise ValueError(e)


########################################## METODOS GUIAS DESPACHO ###################################################
@login_required(login_url='login')
@permission_required('inventario.can_access_crud_guias_despacho', raise_exception=True)
def crud_guia_despacho(request):
    desps = Despacho.objects.all()
    return render(request, 'ventanas_prod/guias_despacho/crud_guia_despacho.html', {'desps': desps})

@login_required(login_url='login')
def editar_guia_despacho(request, despacho_id):
    try:
        actualizar_despacho(despacho_id)
    except ValueError as e:
        return HttpResponse(str(e), status=400)
    
    desp = get_object_or_404(Despacho, despacho_id=despacho_id)
    if request.method == 'POST':
        form = GuiaDespachoForm(request.POST, instance=desp)
        if form.is_valid():                        
            form.save()
            return redirect('/crud_guia_despacho')
            
    else:
        form = GuiaDespachoForm(instance=desp)
    return render(request, 'ventanas_prod/guias_despacho/editar_guia_despacho.html', {'form': form})


########################################## METODOS REPORTE DIARIO ################################################
@login_required(login_url='login')
@permission_required('inventario.can_access_crud_despacho', raise_exception=True)
def crud_reporte(request):
    desps = Despacho.objects.all()
    return render(request, 'ventanas_prod/reporte/crud_reporte.html',{'desps': desps})


########################################## METODOS CERTIFICADO ######################################################

@login_required(login_url='login')
def gen_certificado(request, lote_prod_id):
    # Obtener el objeto correspondiente al lote_prod_id
    odp = get_object_or_404(LoteProd, lote_prod_id=lote_prod_id)
    
    # Renderizar el HTML a una cadena
    html = render_to_string('ventanas_prod/orden_prod/gen_certificado.html', {'odp': odp})

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


"""