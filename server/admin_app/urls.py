from django.urls import path, include
from .views import (
    mostrar_admin, 
    admin_p_agregar,
    admin_m_modificar,
    admin_m_producto, 
    admin_p_eliminar,
    admin_u_aprivilegios, 
    admin_buscar,
    eliminar_usuario,
    modificar_usuario
)
urlpatterns = [
    path('', mostrar_admin, name="admin"),
    path('producto/agregar/', admin_p_agregar, name="agregar_producto"),
    path('productos/', admin_m_producto, name="admin_productos"),
    path('producto/eliminar/<int:fumo_id>', admin_p_eliminar, name="eliminar_producto"),
    path('producto/modificar/<int:fumo_id>', admin_m_modificar, name="modificar_producto"),
    path('producto/buscar', admin_buscar, name="admin_buscar"),
    path('usuarios/', admin_u_aprivilegios, name="mostrar_privilegios"),
    path('usuario/eliminar/<int:id_usuario>', eliminar_usuario, name="eliminar_usuario"),
    path('usuario/modificar/<int:usuario_id>', modificar_usuario, name="modificar_usuario"),
]