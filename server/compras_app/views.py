from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mostrar_compras(request):
    return render(request, 'compras.html')


