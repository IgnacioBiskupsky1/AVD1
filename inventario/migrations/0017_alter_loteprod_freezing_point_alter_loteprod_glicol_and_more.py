# Generated by Django 5.0.4 on 2024-05-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0016_loteprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loteprod',
            name='freezing_point',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='glicol',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='lote_aromatizante',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='lote_asr',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='lote_colorante',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='lote_mp',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='ph',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='loteprod',
            name='volumen_prod',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]