from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm, MpForm, InfoAditivoForm, InForm
from .models import InfoAditivo, Insumo
from django.http import HttpResponse


# Create your views here.

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

def welcome_user(request):
    return render(request, 'usercrud/welcome_user.html')  #BORRAR ESTA COSA

def home(request):
    context={}
    return render(request, 'user/home.html', context)

def login_user(request):
    context={}
    return render(request, 'usercrud/login_user.html', context)

def edituser(request):
    context={}
    return render(request, 'usercrud/edituser.html', context) #BORRAR ESTA COSA











# VIEWS MATERIAS PRIMAS

def crud_mp(request):
    # Obtener parámetros de filtrado y ordenado de la URL
    ordenar_por = request.GET.get('ordenar_por', 'adtv_id,adtv_nom,adtv_dens')

    mps = InfoAditivo.objects.all()

    # Ordenar MP
    ordenar_por_campos = ordenar_por.split(',')
    mps = mps.order_by(*ordenar_por_campos)

    
    return render(request, 'inventary/materia_prima/crud_mp.html', {'mps': mps})



#def crud_mp(request):
#    mps = InfoAditivo.objects.all()
#    return render(request, 'inventary/materia_prima/crud_mp.html', {'mps': mps})

def ingresar_mp(request):
    if request.method == 'POST':
        form = MpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crud_mp')  # Cambia 'home' por el nombre de tu URL de inicio
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









# VIEWS INSUMOS



def crud_insu(request):
    # Obtener parámetros de filtrado y ordenado de la URL
    ordenar_por = request.GET.get('ordenar_por', 'in_nombre,insumo_id')
#   filtrar_cantidad = request.GET.get('filtrar_cantidad', None)

    # Obtener todos los insumos
    insus = Insumo.objects.all()

    # Filtrar insumos si es necesario
#    if filtrar_cantidad is not None:
#        insus = insus.filter(cantidad__gt=0)

    # Ordenar insumos
    ordenar_por_campos = ordenar_por.split(',')
    insus = insus.order_by(*ordenar_por_campos)

    
    return render(request, 'inventary/insumos/crud_insu.html', {'insus': insus})


#def crud_insu(request):
#    insus = Insumo.objects.all()
#    return render(request, 'inventary/crud_insu.html', {'insus': insus}) 




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
