from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',auth_views.LoginView.as_view(),name='login'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('reguser',views.reguser, name='reguser'),
    path('home',views.home, name='home'),
    path('edituser',views.edituser, name='edituser'),
    path('crud_mp',views.crud_mp, name='crud_mp'),
    path('crud_insu',views.crud_insu, name='crud_insu'),

]

