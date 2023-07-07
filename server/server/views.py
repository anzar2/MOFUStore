from django.shortcuts import render
from .forms_demo import *
import fumos_app.models as fumos_app
def mostrar_index(request):
    if request.method == "GET":
        contexto = {
        'form': FormImageDemo()
        }
    if request.method == "POST":
        formulario = FormImageDemo(request.POST, request.FILES)
        if formulario.is_valid():
            formulario_data = formulario.cleaned_data['image']
            fumo = fumos_app.FumoModel(
            fumo_name="prueba",
            release_year =2023,
            fumo_price=1000,
            fumo_size="wena",
            url_img = formulario_data,
            fumo_serie_id = 2,
            stock=2
            )
            fumo.save()
        contexto = {
        'form': FormImageDemo()
        }   
    return render(request, 'index.html', contexto)

def mostrar_productos(request):
    return render(request, 'productos.html')