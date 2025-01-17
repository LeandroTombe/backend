# Generated by Django 5.0.7 on 2024-07-24 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('legajo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('dni', models.IntegerField()),
                ('codCoor', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroCuota', models.IntegerField()),
                ('año', models.IntegerField()),
                ('importe', models.FloatField()),
                ('fechaVencimiento', models.DateField()),
                ('importePagado', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('idMateria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CompromisoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255)),
                ('fechaFirma', models.DateField()),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Inhabilitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('motivo', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Cursado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('cuatrimestre', models.IntegerField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.alumno')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255)),
                ('fechaFirma', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('IDPago', models.IntegerField(primary_key=True, serialize=False)),
                ('montoInformado', models.FloatField()),
                ('fechaPagoInformado', models.DateField()),
                ('montoConfirmado', models.FloatField()),
                ('fechaPagoConfirmado', models.DateField()),
                ('comprobanteDePago', models.CharField(max_length=255)),
                ('formaPago', models.CharField(max_length=255)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.alumno')),
                ('cuota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.cuota')),
            ],
        ),
    ]
