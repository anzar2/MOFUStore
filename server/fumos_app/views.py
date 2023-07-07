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
    cart_form = CartForm()
    contexto = {
        'fumo_model': filter_fumo,
        'cart_form': cart_form
    }
    return render(request, 'productos.html', contexto)

def filtrar_nendoroid(request):
    filter_nendoroid = FumoModel.objects.filter(fumo_serie__id=2)
    cart_form = CartForm()
    contexto = {
        'fumo_model': filter_nendoroid,
        'cart_form': cart_form
    }
    return render(request, 'productos.html', contexto)

def filtrar_puppet(request):
    filter_puppet = FumoModel.objects.filter(fumo_serie__id=3)
    cart_form = CartForm()
    contexto = {
        'fumo_model': filter_puppet,
        'cart_form': cart_form
    }
    return render(request, 'productos.html', contexto)

def filtrar_strap(request):
    filter_strap = FumoModel.objects.filter(fumo_serie__id=4)
    cart_form = CartForm()
    contexto = {
        'fumo_model': filter_strap,
        'cart_form': cart_form
    }
    return render(request, 'productos.html', contexto)

def filtrar_deka(request):
    filter_deka = FumoModel.objects.filter(fumo_serie__id=5)
    cart_form = CartForm()
    contexto = {
        'fumo_model': filter_deka,
        'cart_form': cart_form
    }
    return render(request, 'productos.html', contexto)

def buscar_fumo(request):
    search = request.GET.get('search')
    if search:
        cart_form = CartForm()
        fumos_search = FumoModel.objects.filter(fumo_name__icontains = search)
        contexto = {
            'fumo_model': fumos_search,
            'cart_form': cart_form
        }
    else:
        cart_form = CartForm()
        fumos_all = FumoModel.objects.all()
        contexto = {
            'fumo_model': fumos_all,
            'cart_form': cart_form
        }
   
    return render(request, 'productos.html', contexto)
