from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserInfoModel, RegionModel, CommuneModel
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.models import Count, Sum
import fumos_app.models as fumos_app
from .models import (
    CartDetailModel,
    ShoppingCartModel
)
from datetime import datetime

@login_required
def mostrar_admin(request):
    return render(request, 'base/admin_site.html')

@login_required
def agregar_carrito(request, fumo_id):
    if request.method == 'POST':
        fumo = fumos_app.FumoModel.objects.get(id=fumo_id)
        usuario = User.objects.get(id=request.user.id)
        try:
            cart_user = ShoppingCartModel.objects.get(user_id=request.user.id, status="Pendiente")
            ammount = int(request.POST.get('ammount'))
            last_cart = ShoppingCartModel.objects.filter(user_id=request.user.id).order_by('-creation_date').first()
            if cart_user.status == 'Pendiente':
                for n in range(ammount):
                    if n < 10:
                        new_detail = CartDetailModel(
                        fumo=fumo,
                        shopping_cart=last_cart,
                        user=usuario
                        )
                        new_detail.save()
            else:
                new_cart = ShoppingCartModel(
                creation_date= datetime.now(),
                status="Pendiente",
                user = usuario
                )
                new_cart.save()
                for n in range(ammount):
                    if n < 10:
                        new_detail = CartDetailModel(
                        fumo=fumo,
                        shopping_cart=new_cart,
                        user=usuario
                        )
                        new_detail.save()
        except ObjectDoesNotExist:
            ammount = int(request.POST.get('ammount'))
            new_cart = ShoppingCartModel(
                creation_date= datetime.now(),
                status="Pendiente",
                user = usuario
            )
            new_cart.save()

            for n in range(ammount):
                if n < 10:
                    new_detail = CartDetailModel(
                    fumo=fumo,
                    shopping_cart=new_cart,
                    user=usuario
                    )
                    new_detail.save()
    return redirect('productos')

@login_required
def mostrar_c_realizada(request):
    try:
        cart_detail = CartDetailModel.objects.filter(user_id=request.user.id).values('fumo_id').distinct().annotate(ammount=Count('fumo_id'))
        cart_user = ShoppingCartModel.objects.get(user_id=request.user.id, status="Pendiente")
        for datos in cart_detail:
            fumo = fumos_app.FumoModel.objects.get(id=datos['fumo_id'])
            fumo.stock -= datos['ammount']
            fumo.save()
        cart_user.status = "Confirmado"
        cart_user.save()
        return render(request, 'compra_confirmada.html')
    except:
        if datos['ammount'] > fumo.stock:
            contexto = {
                'mensaje_error': f'No es posible realizar la compra,  la cantidad es superior al stock, la transaccion se ha cancelado.'
            }
        cart_user = ShoppingCartModel.objects.get(user_id=request.user.id, status="Pendiente")
        cart_user.status = "Cancelado"
        cart_user.save()
        return render(request, 'carrito.html', contexto)
@login_required
def mostrar_c_cancelada(request):
    try:
        cart_user = ShoppingCartModel.objects.get(user_id=request.user.id, status="Pendiente")
        cart_user.status = "Cancelada"
        cart_user.save()
        return redirect('index')
    except:
        return redirect('index')
    
@login_required
def quitar_item_carrito(request, fumo_id, shopping_cart_id):
    cart_user = ShoppingCartModel.objects.filter(user_id=request.user.id, status="Pendiente")
    cart_detail_fumo = CartDetailModel.objects.filter(user_id=request.user.id, fumo_id=fumo_id)
    cart_detail = CartDetailModel.objects.filter(user_id=request.user.id, shopping_cart__id=shopping_cart_id)
    cart_detail_fumo.delete()
    # Aqui se supone que la query cart_detail tiene todos los productos agregados al carro, 
    # y si la cantidad de productos del carro es menor a 1, se asume que la compra se cancela
    if cart_detail.count() < 1:
        cart_user = ShoppingCartModel.objects.get(user_id=request.user.id, status="Pendiente")
        cart_user.status = "Cancelado"
        cart_user.save()
    print(cart_detail.count())
    print(cart_detail_fumo.values())
    return redirect('carrito')

@login_required
def mostrar_carrito(request):
    cart_user = ShoppingCartModel.objects.filter(user_id=request.user.id, status="Pendiente")
    cart_detail = CartDetailModel.objects.filter(user_id=request.user.id, shopping_cart__status = "Pendiente").values('fumo_id','fumo__fumo_name','fumo__fumo_price', 'shopping_cart__id').distinct().annotate(ammount=Count('fumo_id'), total=Sum('fumo__fumo_price'))
    total = CartDetailModel.objects.filter(user_id=request.user.id, shopping_cart__status = "Pendiente").aggregate(value=Sum('fumo__fumo_price'))
    existe = cart_user.exists()
    contexto = {
        'tiene_carro': existe,
        'datos_carro': cart_user,
        'detalle': cart_detail,
        'total': total
    }
    return render(request, 'carrito.html', contexto)

def mostrar_login(request):
    if request.method == "GET":
        contexto = {
        'login_form': LoginForm() 
        }
        return render(request, 'login.html', contexto)
    
    if request.method == "POST":
        datos_post = LoginForm(data= request.POST)
        es_Valido = datos_post.is_valid()
        usuario_existe = True
        if es_Valido:
            correo = datos_post.cleaned_data['username']
            password = datos_post.cleaned_data['password']
            usuario = authenticate(request, username=correo, password=password)
            if usuario is not None:
                login(request, usuario)
                print(f'Ingreso el usuario: {correo}')
                return redirect('index')
            else:
                usuario_existe = False

        contexto = {
            'login_form': datos_post,
            'existe': usuario_existe,
            'mensaje_error': 'Asegurate que los campos estén bien escritos'
        }
        return render(request, 'login.html', contexto)

def mostrar_registro(request):
    if request.method == "GET":
        contexto = {
            'registro_form': RegistroForm()
        }
        return render(request, 'registro.html', contexto)
    elif request.method == "POST":
        try:
            registro_form = RegistroForm(request.POST)
            if registro_form.is_valid():
                first_name = registro_form.cleaned_data['first_name']
                last_name = registro_form.cleaned_data['last_name']
                password = registro_form.cleaned_data['password1']
                email = registro_form.cleaned_data['email']
                address = registro_form.cleaned_data['address']
                commune_id = registro_form.cleaned_data['commune']
                region_id = registro_form.cleaned_data['region']

                commune_model = CommuneModel.objects.get(id=commune_id)
                user = User(username=email, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()

                userInfo = UserInfoModel(address=address, commune=commune_model, user=user)
                userInfo.save()

                usuario = authenticate(request, username=email, password=password)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('index')
                else:
                    contexto = {
                        'registro_form': RegistroForm(),
                        'mensaje_error': 'Credenciales inválidas'
                    }
                    return render(request, 'registro.html', contexto)
            else:
                contexto = {
                    'registro_form': registro_form,
                    'mensaje_error': 'Comprueba que los campos cumplan los requerimientos'
                }
                return render(request, 'registro.html', contexto)
        except IntegrityError:
            contexto = {
                'registro_form': RegistroForm(),
                'error_usuario_existente': 'El usuario ingresado ya existe'
            }
            return render(request, 'registro.html', contexto)
    return render(request, 'registro.html')

@login_required
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')