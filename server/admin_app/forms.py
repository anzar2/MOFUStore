from django.forms import (
    Form,
    ModelForm,
    ModelChoiceField,
    CharField,
    TextInput,
    IntegerField,
    NumberInput,
    ImageField,
    FileInput,
    ChoiceField,
    Select,
    CheckboxInput
)
from .data import SERIES_DATA
import fumos_app.models as fumos_app
from django.contrib.auth.models import User
from django.db.utils import ProgrammingError

class AgregarProductoForm(Form):
    fumo_name = CharField(
        max_length=100,
        min_length=1,
        required=True,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'name': 'fumo_name'
            }
        )
    )
    release_year = IntegerField(
        max_value=9999,
        min_value=2000,
        required=True,
        widget= NumberInput(
            attrs={
                'class': 'form-control',
                'name': 'release_year'
            }
        )
    )
    fumo_price = IntegerField(
        max_value=999999,
        min_value=1,
        required=True,
        widget= NumberInput(
            attrs={
                'class': 'form-control',
                'name': 'fumo_price'
            }
        )
    )
    fumo_stock = IntegerField(
        max_value=9999,
        min_value=0,
        help_text="Deja en 0 si aun no tienes stock",
        required=True,
        widget= NumberInput(
            attrs={
                'class': 'form-control',
                'name':'fumo-stock'
            }
        )
    )
    fumo_size = CharField(
        max_length=45,
        min_length=1,
        help_text="Recuerda especificar las dimensiones en centímetros",
        required=True,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'name': 'fumo_size'
            }
        )
    )

    fumo_series = ChoiceField(
        required=True,
        choices=SERIES_DATA,
        widget= Select(
            attrs={
                'class': 'form-select',
                'name':'series'
            }
        )
    )
    
    image = ImageField(
        allow_empty_file=False,
        required=True,
        widget=FileInput(
            attrs={
                'class': 'form-control',
                'name': 'image'
            }
        )
    )

class ModificarProductoForm(ModelForm):
    class Meta:
        model = fumos_app.FumoModel
        fields = [
            'fumo_name',
            'release_year',
            'fumo_price',
            'fumo_size',
            'fumo_serie',
            'stock',
            'url_img',
        ]
        exclude = []
        widgets = {
            'fumo_name': TextInput(attrs={'class': 'form-control'}),
            'release_year': NumberInput(attrs={'class': 'form-control'}),
            'fumo_price': NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fumo_size': TextInput(attrs={'class': 'form-control'}),
            'stock': NumberInput(attrs={'class': 'form-control'}),
            'url_img': FileInput(attrs={'class': 'form-control-file'}),
        }
    fumo_serie = ModelChoiceField(queryset=fumos_app.FumoSeriesModel.objects.all(), widget=Select(attrs={'class': 'form-select'}))