from django.urls import path
from .views import (
   mostrar_compras
)

urlpatterns = [
    path('', mostrar_compras, name="compras"),
]