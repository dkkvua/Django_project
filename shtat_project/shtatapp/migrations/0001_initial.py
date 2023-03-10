# Generated by Django 4.1.5 on 2023-01-14 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(max_length=50)),
                ('object_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Posada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posad_name', models.CharField(max_length=100)),
                ('posad_cod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rota_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vzvod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vzvod_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Zvannya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zvannya_name', models.CharField(max_length=100)),
                ('zvannya_is_officer', models.BooleanField()),
                ('zvannya_is_sergeant', models.BooleanField()),
                ('zvannya_is_soldier', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soldier_name', models.CharField(max_length=150)),
                ('soldier_birthd', models.DateField()),
                ('soldier_osvita', models.CharField(max_length=200)),
                ('soldier_rvk', models.CharField(max_length=200)),
                ('soldier_stan_adres', models.CharField(max_length=250)),
                ('soldier_fin_id', models.IntegerField()),
                ('soldier_zvannya', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shtatapp.zvannya')),
            ],
        ),
        migrations.CreateModel(
            name='Shtat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posad_nomer', models.IntegerField()),
                ('date_priznach', models.DateField()),
                ('object', models.ManyToManyField(related_name='object', to='shtatapp.object')),
                ('objectfact', models.ManyToManyField(related_name='objectfact', to='shtatapp.object')),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shtatapp.rota')),
                ('soldier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shtatapp.soldier')),
                ('vzvod', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shtatapp.vzvod')),
                ('zv_shtat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shtatapp.zvannya')),
            ],
        ),
    ]
