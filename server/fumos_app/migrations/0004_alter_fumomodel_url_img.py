# Generated by Django 4.2.1 on 2023-07-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fumos_app', '0003_fumomodel_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fumomodel',
            name='url_img',
            field=models.ImageField(upload_to='foto_fumo'),
        ),
    ]
