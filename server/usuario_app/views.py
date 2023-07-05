from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserInfoModel, RegionModel, CommuneModel
from django.db.utils import IntegrityError

@login_required
def mostrar_carrito(request):
    contexto = {
        'productos': 1
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
def mostrar_c_realizada(request):
    return render(request, 'compra_confirmada.html')

def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')