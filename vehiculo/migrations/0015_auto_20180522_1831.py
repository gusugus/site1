# Generated by Django 2.0.5 on 2018-05-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0014_auto_20180522_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='user',
        ),
        migrations.AlterField(
            model_name='persona',
            name='username',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
