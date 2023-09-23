from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/login', views.inicio_sesion, name='login'),
    path('auth/registrar', views.registar, name='registrar'),
    path('auth/recuperar', views.recuperar, name='recuperar'),
    path('auth/logout', views.cerrar_sesion, name='logout'),
    
    path('home', views.home, name='home'),

    path('administrador', views.admin, name='admin'),
    
    
    path('data', views.data, name='data'),
]
