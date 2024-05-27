# Generated by Django 5.0.4 on 2024-05-26 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compproducto',
            name='info_aditivo',
        ),
        migrations.RemoveField(
            model_name='compproducto',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='stockaditivo',
            name='nomAditivo',
        ),
        migrations.DeleteModel(
            name='Insumo',
        ),
        migrations.RemoveField(
            model_name='stockproducto',
            name='producto',
        ),
        migrations.DeleteModel(
            name='CompProducto',
        ),
        migrations.DeleteModel(
            name='InfoAditivo',
        ),
        migrations.DeleteModel(
            name='StockAditivo',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='StockProducto',
        ),
    ]
