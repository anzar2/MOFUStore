from django.db.models import (
    Model,
    CharField,
    OneToOneField,
    ForeignKey,
    CASCADE
)
from django.contrib.auth.models import User

class RegionModel(Model):
    region_name = CharField(max_length=64, blank=False, null=False)

class CommuneModel(Model):
    commune_name = CharField(max_length=64, blank=False, null=False)
    region = ForeignKey(RegionModel, on_delete=CASCADE)

class UserInfoModel(Model):
    address = CharField(max_length=100, null=False, blank=False)
    commune = ForeignKey(CommuneModel, on_delete=CASCADE)
    user = OneToOneField(User, on_delete=CASCADE)