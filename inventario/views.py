from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm, MpForm, InfoAditivoForm, InForm, ProductosForm, CompProductoForm
from .models import InfoAditivo, Insumo, Productos, CompProducto
from django.http import HttpResponse


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
        form = MpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_mp')  
    else:
        form = MpForm()
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
        form = InForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_insu')  # Cambia 'home' por el nombre de tu URL de inicio
    else:
        form = InForm()
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
        form = InForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('/crud_insu')  
    else:
        form = InForm(instance=insumo)
    return render(request, 'inventary/insumos/editar_insumo.html', {'form': form})

##################################### METODOS PRODUCTO #####################################

def crud_producto(request):
    productos = Productos.objects.all()
    return render(request, 'inventary/productos/crud_producto.html', {'productos': productos}) 

def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto')  # Cambia 'home' por el nombre de tu URL de inicio
    else:
        form = ProductosForm()
    return render(request, 'inventary/productos/ingresar_producto.html', {'form': form})

def editar_producto(request, productos_id):
    producto = get_object_or_404(Productos, productos_id=productos_id)
    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/crud_producto')  
    else:
        form = ProductosForm(instance=producto)
    return render(request, 'inventary/productos/editar_producto.html', {'form': form})

def eliminar_producto(request, productos_id):
    producto = get_object_or_404(Productos, productos_id=productos_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/crud_producto')  # Redirigir a la página de listado de productos
    return render(request, 'inventary/productos/eliminar_producto.html', {'producto': producto})

##################################### METODOS COMPOSICION #####################################

#def crud_comp(request):
#    comps = CompProducto.objects.all()
#    return render(request, 'inventary/comp_producto/crud_comp.html', {'comps': comps}) 

def crud_comp(request):
    
    producto_seleccionado = request.GET.get('producto', None)
    
    if producto_seleccionado:
        comps = CompProducto.objects.filter(productos__productos_nom = producto_seleccionado)
    else:
        comps = CompProducto.objects.all()
    
    productos = CompProducto.objects.values_list('productos__productos_nom', flat=True).distinct()
    
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