
from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
#from .views import producir_producto_view

app_name = 'inventario'


urlpatterns = [
    path('', views.login_user,  name='login_user'),
    path('<int:pk>/', views.user_detail, name='user_detail'),
    path('new/', views.user_create, name='user_create'),
    path('<int:pk>/edit/', views.edituser, name='edituser'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('home/', views.home, name='home'),
    path('<int:pk>/update', views.user_update, name='user_update'),
    path('login_user/', views.login_user, name='login_user'),
    path('user_list/', views.user_list,  name='user_list'),

    path('admin/', admin.site.urls),

    path('welcome_user/',views.welcome_user, name='welcome_user'),
    path('cruds/',views.cruds, name='cruds'),

    path('ingresar_mp/',views.ingresar_mp, name='ingresar_mp'),
    path('editar_mp/<int:adtv_id>/',views.editar_mp, name='editar_mp'),
    path('eliminar_mp/<int:adtv_id>/', views.eliminar_mp, name='eliminar_mp'),
    path('listar_mp',views.listar_mp, name='listar_mp'),
    path('crud_mp/', views.crud_mp, name='crud_mp'),


    path('listar_in',views.listar_in, name='listar_in'),
    path('ingresar_insumo',views.ingresar_in, name='ingresar_insumo'),
    path('eliminar_insumo/<int:insumo_id>/',views.eliminar_in, name='eliminar_insumo'),
    path('editar_insumo/<int:insumo_id>/',views.editar_in, name='editar_insumo'),
    path('crud_insu/', views.crud_insu, name='crud_insu'),
   
    path('crud_producto/', views.crud_producto, name='crud_producto'),
    path('ingresar_producto/',views.ingresar_producto, name='ingresar_producto'),
    path('editar_producto/<int:producto_id>/',views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/',views.eliminar_producto, name='eliminar_producto'),
    
    
    path('crud_comp/', views.crud_comp, name='crud_comp'),
    path('ingresar_comp/',views.ingresar_comp, name='ingresar_comp'),
    path('editar_comp/<int:comp_producto_id>/',views.editar_comp, name='editar_comp'),
    path('eliminar_comp/<int:comp_producto_id>/',views.eliminar_comp, name='eliminar_comp'),

    path('crud_producto_copec/', views.crud_producto_copec, name='crud_producto_copec'),
    path('ingresar_producto_copec/',views.ingresar_producto_copec, name='ingresar_producto_copec'),
    path('editar_producto_copec/<int:prod_copec_id>/',views.editar_producto_copec, name='editar_producto_copec'),
    path('eliminar_producto_copec/<int:prod_copec_id>/',views.eliminar_producto_copec, name='eliminar_producto_copec'),

    #path('producir/', views.producir_producto_view, name='producir_producto'),
    #path('orden_de_prod/', views.orden_de_prod, name='orden_de_prod'),

    path('crud_stock_prod/', views.crud_stock_prod, name='crud_stock_prod'),
    path('ingresar_stock_prod/',views.ingresar_stock_prod, name='ingresar_stock_prod'),
    path('editar_stock_prod/<int:stock_producto_id>/',views.editar_stock_prod, name='editar_stock_prod'),
    
    
    path('crud_stock_mp/', views.crud_stock_mp, name='crud_stock_mp'),
    path('ingresar_stock_mp/',views.ingresar_stock_mp, name='ingresar_stock_mp'),
    path('editar_stock_mp/<int:stock_ad_id>/',views.editar_stock_mp, name='editar_stock_mp'),
    
    path('crud_stock_insumo/', views.crud_stock_insumo, name='crud_stock_insumo'),
    path('ingresar_stock_insumo/',views.ingresar_stock_insumo, name='ingresar_stock_insumo'),
    path('editar_stock_insumo/<int:stock_in_id>/',views.editar_stock_insumo, name='editar_stock_insumo'),

    path('crud_orden_prod/', views.crud_orden_prod, name='crud_orden_prod'),
    path('ingresar_orden_prod/',views.ingresar_orden_prod, name='ingresar_orden_prod'),
    path('editar_orden_prod/<int:lote_prod_id>/',views.editar_orden_prod, name='editar_orden_prod'),

    path('crud_calidad/', views.crud_calidad, name='crud_calidad'),
    path('editar_calidad/<int:lote_prod_id>/',views.editar_calidad, name='editar_calidad'),
    path('confirmar_prod_calidad/<int:lote_prod_id>/',views.confirmar_prod_calidad, name='confirmar_prod_calidad'),
    

    path('crud_certificado/', views.crud_certificado, name='crud_certificado'),
    path('gen_certificado/<int:lote_prod_id>/', views.gen_certificado, name='gen_certificado'),
    ]

