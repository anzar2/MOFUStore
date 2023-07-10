from django.urls import path, include

from .views import (
    mostrar_login,
    mostrar_registro,
    mostrar_c_realizada,
    cerrar_sesion,
    mostrar_carrito,
    agregar_carrito,
    mostrar_c_cancelada,
    quitar_item_carrito
)

urlpatterns = [
    path('entrar/', mostrar_login, name='login'),
    path('crear/', mostrar_registro, name='registro'),
    path('micarro/', mostrar_carrito, name="carrito"),
    path('micarro/agregar/<int:fumo_id>/', agregar_carrito, name="agregar_carro"),
    path('compra_realizada/', mostrar_c_realizada, name='compra_realizada'),
    path('compra_cancelada/', mostrar_c_cancelada, name='compra_cancelada'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('quitar_item_carro/<int:fumo_id>/<int:shopping_cart_id>', quitar_item_carrito, name='quitar_item'),
    path('admin/', include('admin_app.urls'))
]