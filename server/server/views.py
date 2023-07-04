from django.shortcuts import render

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_contacto(request):
    return render(request, 'contacto.html')

def mostrar_login(request):
    return render(request, 'login.html')

def mostrar_promo(request):
    return render(request, 'promociones.html')

def mostrar_productos(request):
    return render(request, 'productos.html')