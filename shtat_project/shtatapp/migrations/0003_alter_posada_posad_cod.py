# Generated by Django 4.1.5 on 2023-01-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shtatapp', '0002_alter_rota_rota_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posada',
            name='posad_cod',
            field=models.CharField(max_length=20),
        ),
    ]
