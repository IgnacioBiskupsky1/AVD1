# Generated by Django 5.0.4 on 2024-06-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_compproducto_pp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loteprod',
            name='estado_aceptado',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='estado_produccion',
            field=models.CharField(default='PENDIENTE', max_length=100),
        ),
    ]
