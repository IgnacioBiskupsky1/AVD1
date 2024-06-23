# Generated by Django 5.0.4 on 2024-06-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_loteprod_apariencia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='insumo_cajas_por_pallet',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='insumo_env_por_caja',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='insumo_vol',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
    ]