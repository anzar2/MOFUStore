from django.shortcuts import render
from .models import FumoModel, FumoSeriesModel
from usuario_app.forms import CartForm

def mostrar_productos(request):
    fumos_all = FumoModel.objects.all()
    cart_form = CartForm()

    contexto = {
        'fumo_model': fumos_all,
        'cart_form': cart_form
    }
    return render(request, 'productos.html', contexto)

def filtrar_fumo(request):
    filter_fumo = FumoModel.objects.filter(fumo_serie__id=1)
    contexto = {
        'fumo_model': filter_fumo
    }
    return render(request, 'productos.html', contexto)

def filtrar_nendoroid(request):
    filter_nendoroid = FumoModel.objects.filter(fumo_serie__id=2)
    contexto = {
        'fumo_model': filter_nendoroid
    }
    return render(request, 'productos.html', contexto)

def filtrar_puppet(request):
    filter_puppet = FumoModel.objects.filter(fumo_serie__id=3)
    contexto = {
        'fumo_model': filter_puppet
    }
    return render(request, 'productos.html', contexto)

def filtrar_strap(request):
    filter_strap = FumoModel.objects.filter(fumo_serie__id=4)
    contexto = {
        'fumo_model': filter_strap
    }
    return render(request, 'productos.html', contexto)

def filtrar_deka(request):
    filter_deka = FumoModel.objects.filter(fumo_serie__id=5)
    contexto = {
        'fumo_model': filter_deka
    }
    return render(request, 'productos.html', contexto)

def buscar_fumo(request):
    search = request.GET.get('search')
    if search:
        fumos_search = FumoModel.objects.filter(fumo_name__icontains = search)
        contexto = {
        'fumo_model': fumos_search
        }
    else:
        fumos_all = FumoModel.objects.all()
        contexto = {
            'fumo_model': fumos_all
        }
   
    return render(request, 'productos.html', contexto)
