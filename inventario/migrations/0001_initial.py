# Generated by Django 5.0.4 on 2024-06-12 22:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAditivo',
            fields=[
                ('adtv_id', models.AutoField(primary_key=True, serialize=False)),
                ('adtv_nom', models.CharField(blank=True, max_length=60, null=True, unique=True)),
                ('adtv_dens', models.DecimalField(decimal_places=5, default=0.0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('insumo_id', models.AutoField(primary_key=True, serialize=False)),
                ('insumo_nom', models.CharField(blank=True, max_length=60, null=True)),
                ('insumo_vol', models.DecimalField(decimal_places=1, max_digits=3)),
                ('insumo_env_por_caja', models.DecimalField(decimal_places=1, max_digits=3)),
                ('insumo_cajas_por_pallet', models.DecimalField(decimal_places=1, max_digits=3)),
                ('insumo_desc', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoteProd',
            fields=[
                ('lote_prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('lote_prod_fecha', models.DateField(default=datetime.date.today)),
                ('volumen_odp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volumen_prod', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cant_prod', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('tk_agua', models.CharField(default='N/A', max_length=5)),
                ('tk_prod', models.CharField(default='N/A', max_length=5)),
                ('lote_mp', models.CharField(default='N/A', max_length=5)),
                ('fecha_ven_mp', models.DateField(default=datetime.date.today)),
                ('lote_colorante', models.CharField(default='N/A', max_length=5)),
                ('fecha_ven_colorante', models.DateField(default=datetime.date.today)),
                ('lote_aromatizante', models.CharField(default='N/A', max_length=5)),
                ('fecha_ven_aromatizante', models.DateField(default=datetime.date.today)),
                ('num_pedido_asr', models.CharField(default='N/A', max_length=5)),
                ('lote_asr', models.CharField(default='N/A', max_length=5)),
                ('fecha_ven_asr', models.DateField(default=datetime.date.today)),
                ('freezing_point', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('ph', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('glicol', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('color', models.CharField(default='N/A', max_length=10)),
                ('olor', models.CharField(default='N/A', max_length=10)),
                ('apariencia', models.CharField(default='N/A', max_length=5)),
                ('sellos_tapas', models.CharField(default='N/A', max_length=5)),
                ('valvulas', models.CharField(default='N/A', max_length=5)),
                ('estado_aceptado', models.CharField(default='-', max_length=10)),
                ('estado_produccion', models.CharField(default='PENDIENTE', max_length=10)),
                ('patente', models.CharField(default='N/A', max_length=5)),
                ('cliente', models.CharField(default='COPEC', max_length=50)),
            ],
            options={
                'permissions': [('can_access_crud_orden_prod', 'Can access crud_orden_prod view'), ('can_access_crud_calidad', 'Can access crud_calidad view'), ('can_access_crud_lote_desp', 'Can access crud_lote_desp view')],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('producto_nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('despacho_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_despacho', models.DateField(default=datetime.date.today)),
                ('tipo_despacho', models.CharField(default='Despacho', max_length=50)),
                ('cant_despacho', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('guia_despacho', models.IntegerField(default=0)),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.loteprod')),
            ],
            options={
                'permissions': [('can_access_crud_guias_despacho', 'Can access crud_guias_despacho view'), ('can_access_crud_despacho', 'Can access crud_despacho view')],
            },
        ),
        migrations.CreateModel(
            name='ProdCopec',
            fields=[
                ('prod_copec_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_copec_cod', models.CharField(blank=True, max_length=10, null=True)),
                ('prod_copec_nom', models.CharField(blank=True, max_length=60, null=True)),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.insumo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
        migrations.AddField(
            model_name='loteprod',
            name='prod_copec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.prodcopec'),
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
                ('stock_ad_cant_lt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nomAditivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.infoaditivo')),
            ],
            options={
                'permissions': [('can_access_crud_stock_mp', 'Can access crud_stock_mp view')],
            },
        ),
        migrations.CreateModel(
            name='StockInsumo',
            fields=[
                ('stock_in_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_in_cant_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.insumo')),
            ],
            options={
                'permissions': [('can_access_crud_stock_insumo', 'Can access crud_stock_insumo view')],
            },
        ),
        migrations.CreateModel(
            name='StockProducto',
            fields=[
                ('stock_producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_prod_cant_vol', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_prod_cant_uni', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prod_copec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.prodcopec')),
            ],
        ),
    ]
