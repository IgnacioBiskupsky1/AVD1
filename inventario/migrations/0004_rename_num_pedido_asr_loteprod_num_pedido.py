# Generated by Django 5.0.4 on 2024-06-21 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_loteprod_estado_aceptado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loteprod',
            old_name='num_pedido_asr',
            new_name='num_pedido',
        ),
    ]