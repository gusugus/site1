# Generated by Django 2.0.5 on 2018-05-22 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0012_auto_20180522_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='carro',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.DO_NOTHING, to='vehiculo.Carro'),
        ),
    ]
