from django.db.models import (
    Model,
    CharField,
    OneToOneField,
    ForeignKey,
    DateField,
    PositiveSmallIntegerField,
    CASCADE
)
from django.contrib.auth.models import User
import fumos_app.models as fumos_app

class RegionModel(Model):
    region_name = CharField(max_length=64, blank=False, null=False)

class CommuneModel(Model):
    commune_name = CharField(max_length=64, blank=False, null=False)
    region = ForeignKey(RegionModel, on_delete=CASCADE)

class UserInfoModel(Model):
    address = CharField(max_length=100, null=False, blank=False)
    commune = ForeignKey(CommuneModel, on_delete=CASCADE)
    user = OneToOneField(User, on_delete=CASCADE)

class ShoppingCartModel(Model):
    creation_date = DateField(null=False, blank=False)
    status = CharField(max_length=25, blank=False, null=False)
    user = ForeignKey(User, on_delete=CASCADE)

class CartDetailModel(Model):
    fumo = ForeignKey(fumos_app.FumoModel, on_delete=CASCADE)
    shopping_cart = ForeignKey(ShoppingCartModel, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
