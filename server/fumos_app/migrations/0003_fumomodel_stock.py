# Generated by Django 4.2.1 on 2023-07-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fumos_app', '0002_alter_fumomodel_fumo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fumomodel',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
