from django.contrib import admin
from django.urls import path, include
from .views import (
    mostrar_productos,
    filtrar_fumo,
    filtrar_deka,
    filtrar_nendoroid,
    filtrar_puppet,
    filtrar_strap,
    buscar_fumo
)

urlpatterns = [
    path('', mostrar_productos,name='productos'),
    path('Fumo/', filtrar_fumo,name='filtro_fumo'),
    path('Nendoroid/', filtrar_nendoroid,name='filtro_nendoroid'),
    path('Puppet/', filtrar_puppet,name='filtro_puppet'),
    path('Strap/', filtrar_strap,name='filtro_strap'),
    path('Deka/', filtrar_deka,name='filtro_deka'),
    path('buscar/', buscar_fumo,name='buscar'),
]
