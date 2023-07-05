from django.urls import path, include
from .views import (
    mostrar_login,
    mostrar_registro,
    mostrar_c_realizada,
    cerrar_sesion,
    mostrar_carrito
)

urlpatterns = [
    path('entrar/', mostrar_login, name='login'),
    path('crear/', mostrar_registro, name='registro'),
    path('miscompras/', include('compras_app.urls')),
    path('micarro/', mostrar_carrito, name="carrito"),
    path('compra_realizada/', mostrar_c_realizada, name='compra_realizada'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]