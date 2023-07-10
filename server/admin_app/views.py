from django.shortcuts import render, redirect
from .forms import AgregarProductoForm, ModificarProductoForm
import fumos_app.models as fumos_app
import usuario_app.models as usuario_app
from django.contrib.auth.models import User

# Create your views here.
def mostrar_admin(request):
    return render(request, 'admin_index.html')

def admin_p_agregar(request):
    if request.method == "POST":
        datos_post = AgregarProductoForm(request.POST, request.FILES)
        if datos_post.is_valid():
            fumo_name = datos_post.cleaned_data['fumo_name']
            release_year = datos_post.cleaned_data['release_year']
            fumo_price = datos_post.cleaned_data['fumo_price']
            fumo_stock = datos_post.cleaned_data['fumo_stock']
            fumo_size = datos_post.cleaned_data['fumo_size']
            image = datos_post.cleaned_data['image']
            fumo_serie = datos_post.cleaned_data['fumo_series']
            serie_model = fumos_app.FumoSeriesModel.objects.filter(id=int(fumo_serie)).values('id').get()
            new_fumo = fumos_app.FumoModel(
                fumo_name=fumo_name,
                release_year=release_year,
                fumo_price=fumo_price,
                stock=fumo_stock,
                fumo_size=fumo_size,
                url_img=image,
                fumo_serie_id=serie_model['id']
            )
            new_fumo.save()
            print(fumo_serie)
            return redirect('admin_productos')
        else:
            print(datos_post.errors)

    agregar_form = AgregarProductoForm()
    contexto = {
        'formulario': agregar_form,
    }
    return render(request, 'admin_p_agregar.html', contexto)

def admin_m_producto(request):
    fumos_all = fumos_app.FumoModel.objects.all().values('id', 'fumo_name','release_year','fumo_price','fumo_size', 'fumo_serie__name_series', 'stock').order_by('-id')
    contexto = {
        'fumo_model': fumos_all
    }
    return render(request, 'admin_productos.html', contexto)

def admin_m_modificar(request, fumo_id):
    fumo = fumos_app.FumoModel.objects.get(id=fumo_id)
    contexto = {
        'formulario': ModificarProductoForm(instance=fumo)
    }
    if request.method == "POST":
        datos_formulario = ModificarProductoForm(request.POST, request.FILES, instance=fumo)
        if datos_formulario.is_valid():
            mod_fumo = datos_formulario.save()
            return redirect('admin_productos')
    return render(request, 'admin_p_modificar.html', contexto)

def admin_p_eliminar(request, fumo_id):
    fumo_delete = fumos_app.FumoModel.objects.get(id=fumo_id)
    fumo_delete.delete()
    return redirect('admin_productos')

def admin_buscar(request):
    search = request.GET.get('search-admin')
    if search:

        fumos_search = fumos_app.FumoModel.objects.filter(fumo_name__icontains = search)
        contexto = {
            'fumo_model': fumos_search,
        }
    else:

        fumos_all = fumos_app.FumoModel.objects.all()
        contexto = {
            'fumo_model': fumos_all,
        }
    return render(request, 'admin_productos.html', contexto)

def admin_u_aprivilegios(request):
    usuario_sesion = User.objects.get(id=request.user.id)
    if usuario_sesion.is_superuser == 0:
        usuarios = User.objects.filter(is_superuser=0)
    else:
        usuarios = User.objects.all()

    contexto = {
        'usuarios': usuarios,
        'usuario_sesion': usuario_sesion.id
    }
    return render(request, 'admin_u_aprivilegios.html', contexto)

def eliminar_usuario(request, id_usuario):
    usuario_delete = User.objects.get(id=id_usuario)
    usuario_delete.delete()
    usuario_delete.save()
    return redirect('mostrar_privilegios')

def modificar_usuario(request, usuario_id):
    usuario = User.objects.get(id=usuario_id)
    print(usuario.is_staff == 1)
    if usuario.is_staff == 1:
        usuario.is_staff = 0
        usuario.save()
    else:
        usuario.is_staff = 1
        usuario.save()

    return redirect('mostrar_privilegios')