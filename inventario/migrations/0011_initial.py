# Generated by Django 5.0.4 on 2024-05-26 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0010_remove_compproducto_info_aditivo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAditivo',
            fields=[
                ('adtv_id', models.AutoField(primary_key=True, serialize=False)),
                ('adtv_nom', models.CharField(blank=True, max_length=60, null=True)),
                ('adtv_dens', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('insumo_id', models.AutoField(primary_key=True, serialize=False)),
                ('in_nombre', models.CharField(blank=True, max_length=60, null=True)),
                ('in_volumen', models.DecimalField(decimal_places=1, max_digits=4)),
                ('in_cant_por_pallet', models.DecimalField(decimal_places=1, max_digits=3)),
                ('in_desc', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('producto_nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CompProducto',
            fields=[
                ('comp_producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('pp', models.DecimalField(decimal_places=5, max_digits=5)),
                ('vv', models.DecimalField(decimal_places=5, default=1.0, max_digits=6)),
                ('info_aditivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.infoaditivo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
        migrations.CreateModel(
            name='StockAditivo',
            fields=[
                ('stock_ad_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_ad_cant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nomAditivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.infoaditivo')),
            ],
        ),
        migrations.CreateModel(
            name='StockProducto',
            fields=[
                ('stock_producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_prod_cant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
    ]
