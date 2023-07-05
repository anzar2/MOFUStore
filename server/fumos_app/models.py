from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    CASCADE
)
from django.contrib.auth.models import User

class FumoSeriesModel(Model):
    name_series = CharField(max_length=45, null=False, blank=False)

class FumoModel(Model):
    fumo_name = CharField(max_length=45, null=False, blank=False)
    release_year = PositiveSmallIntegerField(null=False, blank=False)
    fumo_price = PositiveIntegerField(null=False, blank=False)
    fumo_size = CharField(max_length=45, null=False, blank=False)
    fumo_serie = ForeignKey(FumoSeriesModel, on_delete=CASCADE)
    url_img = CharField(max_length=50, null=False, blank=False)
    
