from django.urls import path
from .views import (
    mostrar_login,
    mostrar_registro,
    mostrar_c_realizada,
    cerrar_sesion
)

urlpatterns = [
    path('entrar/', mostrar_login, name='login'),
    path('crear/', mostrar_registro, name='registro'),
    path('compra_realizada/', mostrar_c_realizada, name='compra_realizada'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]