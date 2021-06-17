# Generated by Django 3.2.4 on 2021-06-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boleta',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('rut', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='gasto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('fecha', models.DateField()),
                ('cantidadActual', models.IntegerField()),
                ('cantidadMinima', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('rut', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.IntegerField()),
                ('rutCliente', models.IntegerField()),
            ],
        ),
    ]