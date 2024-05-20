from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usercrud'

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
    path('welcome_user/',views.welcome_user, name='welcome_user'),

    path('ingresar_mp/',views.ingresar_mp, name='ingresar_mp'),
    path('editar_mp/<int:adtv_id>/',views.editar_mp, name='editar_mp'),
    path('eliminar_mp/<int:adtv_id>/', views.eliminar_mp, name='eliminar_mp'),
    path('listar_mp',views.listar_mp, name='listar_mp'),
    path('listar_in',views.listar_in, name='listar_in'),
    path('ingresar_insumo',views.ingresar_in, name='ingresar_insumo'),
    path('eliminar_insumo/<int:insumo_id>/',views.eliminar_in, name='eliminar_insumo'),
    path('editar_insumo/<int:insumo_id>/',views.editar_in, name='editar_insumo'),
    path('crud_insu/', views.crud_insu, name='crud_insu'),
    path('crud_mp/', views.crud_mp, name='crud_mp'),
    

]

