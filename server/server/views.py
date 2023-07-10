from django.shortcuts import render
def mostrar_index(request):  
    return render(request, 'index.html')

def mostrar_productos(request):
    return render(request, 'productos.html')